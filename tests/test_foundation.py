from datetime import datetime, timedelta
import json
from pathlib import Path
import pytest
from mdsquare_trading.domain import Candle, IST, aggregate
from mdsquare_trading.store import Store
from mdsquare_trading.service import assign, context, submit
from mdsquare_trading.providers.upstox import Upstox, MarketDataError
from mdsquare_trading.policy import validate_candidate, economics
from mdsquare_trading.engine import advance

T = datetime(2026,10,16,9,15,tzinfo=IST)


def bar(i, low=98, high=105, opening=100, close=102, observed=None):
    start=T+timedelta(minutes=i)
    return Candle('NIFTY',start,1,opening,high,low,close,observed or start+timedelta(minutes=1))


@pytest.fixture
def store(tmp_path):
    s=Store(tmp_path/'test.sqlite3')
    yield s
    s.close()


@pytest.fixture
def policy():
    p=json.loads(Path('config/paper.json').read_text())
    p.update(paper_policy_registered=True,stop_buffer_points=1,round_trip_cost_points=0.1,minimum_reward_risk=1)
    p['categories']['breakout']=True
    p['setups']['breakout_continuation_long']=True
    return p


def job(store,policy):
    store.ingest([bar(i) for i in range(5)])
    assign(store,'chatgpt')
    return context(store,'NIFTY',policy,T+timedelta(minutes=5,seconds=5))


def candidate(j):
    b=j['five_minute'][0]['id']
    return {'setup':'breakout_continuation_long','regime':'BULL_TREND','direction':'LONG','location':'BREAKOUT',
            'trade_intent':'SWING','entry':106,'stop':97,'target':119,'expires_at':(T+timedelta(minutes=15)).isoformat(),
            'evidence_bar_ids':[b],'correction_bar_ids':[b],
            'projection':{'method':'SPIKE_EXTENSION','anchors':[{'bar_id':b,'field':'low'},{'bar_id':b,'field':'close'}]},
            **{k:'Hypothetical unit-test evidence; not a trade recommendation' for k in
               ('context_reason','sequence_reason','contradiction','stop_reason','target_reason','opposition_reason')}}


def test_only_complete_session_aligned_bars():
    bars=[bar(i) for i in range(5)]
    assert not aggregate(bars,T+timedelta(minutes=5,seconds=4))
    result=aggregate(bars,T+timedelta(minutes=5,seconds=5))
    assert len(result)==1 and result[0].start==T
    assert not aggregate(bars[:2]+bars[3:],T+timedelta(minutes=6))
    assert not aggregate([bar(0,observed=T+timedelta(days=1)),*bars[1:]],T+timedelta(minutes=6))


def test_nan_bad_ohlc_and_naive_rejected():
    with pytest.raises(ValueError):bar(0,high=float('nan'))
    with pytest.raises(ValueError):bar(0,low=110)
    with pytest.raises(ValueError):Candle('NIFTY',T.replace(tzinfo=None),1,100,105,98,102,T)


def test_idempotent_ingestion_and_correction(store):
    store.ingest([bar(0)])
    store.ingest([bar(0,observed=T+timedelta(hours=1))])
    assert store.candles('NIFTY',1)[0].observed_at==T+timedelta(minutes=1)
    store.ingest([bar(0,low=97,observed=T+timedelta(hours=1))])
    assert store.candles('NIFTY',1)[0].low==97
    assert store.db.execute('SELECT count(*) FROM events').fetchone()[0]==1


def test_context_gaps_and_daily_causality(store,policy):
    j=job(store,policy)
    assert j['data_quality']['status']=='READY'
    later=context(store,'NIFTY',policy,T+timedelta(minutes=10,seconds=5))
    assert later['data_quality']['status']=='INCOMPLETE'
    store.ingest([Candle('NIFTY',T.replace(hour=0,minute=0),1440,100,105,98,102,T)])
    assert not context(store,'NIFTY',policy,T+timedelta(minutes=5,seconds=5))['daily']


def test_economics_unknown_probability():
    e=economics(100,90,120,1)
    assert e['break_even_probability']==pytest.approx(11/30)
    assert e['estimated_success_probability'] is None and not e['positive_expectancy_established']


def test_projection_and_stop_cannot_be_manufactured(store,policy):
    j=job(store,policy); c=candidate(j)
    # 102+(102-98)=106, not 119: reject an inflated target.
    with pytest.raises(ValueError,match='projection'):validate_candidate(c,j,policy)
    c['projection']={'method':'SPIKE_EXTENSION','anchors':[{'bar_id':j['five_minute'][0]['id'],'field':'low'},{'bar_id':j['five_minute'][0]['id'],'field':'high'}]}
    c['target']=112
    c['stop']=99
    with pytest.raises(ValueError,match='protect'):validate_candidate(c,j,policy)
    c['stop']=97
    policy['categories']['breakout']=False
    with pytest.raises(ValueError,match='disabled'):validate_candidate(c,j,policy)


def test_handover_rejects_old_processor_and_duplicates(store,policy):
    j=job(store,policy)
    review={'context_id':j['context_id'],'processor_id':'chatgpt','generation':1,'action':'WAIT','reason':'Developing','open_trade_reviews':[]}
    submit(store,review,policy,T+timedelta(minutes=5,seconds=10))
    with pytest.raises(ValueError,match='already reviewed'):submit(store,review,policy,T+timedelta(minutes=5,seconds=11))
    assign(store,'claude')
    with pytest.raises(ValueError,match='processor'):submit(store,review,policy,T+timedelta(minutes=5,seconds=12))


def test_context_correction_rejected(store,policy):
    j=job(store,policy)
    store.ingest([bar(0,low=97,observed=T+timedelta(minutes=6))])
    review={'context_id':j['context_id'],'processor_id':'chatgpt','generation':1,'action':'WAIT','reason':'Developing','open_trade_reviews':[]}
    with pytest.raises(ValueError,match='changed'):submit(store,review,policy,T+timedelta(minutes=6))


def test_paper_protection_and_ambiguous_intrabar(store,policy):
    p={'id':'p','instrument':'NIFTY','status':'OPEN','direction':'LONG','entry':100,'fill_price':100,
       'stop':90,'target':120,'created_at':T.isoformat(),'expires_at':(T+timedelta(minutes=10)).isoformat()}
    with store.db:store.save_plan(p)
    store.ingest([bar(0,low=89,high=121,close=100)])
    events=advance(store,policy,T+timedelta(minutes=1))
    assert events[0]['type']=='AMBIGUOUS_INTRAMINUTE_ORDER'
    assert store.plans(True)[0]['status']=='REVIEW_REQUIRED'
    assert not advance(store,policy,T+timedelta(minutes=2))


def test_gap_stop_uses_worse_open(store,policy):
    p={'id':'p','instrument':'NIFTY','status':'OPEN','direction':'LONG','entry':100,'fill_price':100,
       'stop':90,'target':120,'created_at':T.isoformat(),'expires_at':(T+timedelta(minutes=10)).isoformat()}
    with store.db:store.save_plan(p)
    store.ingest([bar(0,low=84,high=89,opening=85,close=86)])
    advance(store,policy,T+timedelta(minutes=1))
    assert store.plans()[0]['exit_price']==85
    assert store.plans()[0]['net_points']==pytest.approx(-15.1)


class Response:
    def __init__(self,status,payload=None):self.status_code,self.payload=status,payload
    def json(self):return self.payload


class Session:
    def __init__(self,responses):self.responses,self.calls=list(responses),[]
    def get(self,url,**kw):self.calls.append((url,kw));return self.responses.pop(0)


def test_upstox_v3_encoded_instrument_and_retry():
    s=Session([Response(429),Response(200,{'status':'success','data':{'candles':[[T.isoformat(),100,105,98,102,0,0]]}})])
    result=Upstox('TEST_TOKEN',s,sleep=lambda _:None).intraday('NIFTY',T+timedelta(minutes=1))
    assert len(result)==1 and '%7C' in s.calls[0][0] and '/v3/historical-candle/intraday/' in s.calls[0][0]
    assert s.calls[0][1]['allow_redirects'] is False


def test_auth_does_not_retry_or_echo_token():
    s=Session([Response(401)])
    with pytest.raises(MarketDataError) as e:Upstox('SECRET',s).intraday('NIFTY',T)
    assert len(s.calls)==1 and 'SECRET' not in str(e.value)


def valid_job_and_review(store,policy):
    store.ingest([bar(i,low=95,high=110) if i<5 else bar(i,low=98,high=104) for i in range(10)])
    assign(store,'chatgpt')
    j=context(store,'NIFTY',policy,T+timedelta(minutes=10,seconds=5))
    c=candidate(j)
    first,last=j['five_minute'][0]['id'],j['five_minute'][-1]['id']
    c.update(entry=105,stop=97,target=125,correction_bar_ids=[last],evidence_bar_ids=[first,last],
             projection={'method':'SPIKE_EXTENSION','anchors':[{'bar_id':first,'field':'low'},{'bar_id':first,'field':'high'}]})
    return j,{'context_id':j['context_id'],'processor_id':'chatgpt','generation':1,'action':'CANDIDATE',
              'reason':'Hypothetical fixture','open_trade_reviews':[],'candidate':c}


def test_candidate_persists_then_real_subsequent_paper_events(store,policy):
    j,review=valid_job_and_review(store,policy)
    submit(store,review,policy,T+timedelta(minutes=10,seconds=10))
    assert store.plans()[0]['status']=='PENDING'
    store.ingest([bar(11,low=100,high=108,opening=102,close=107),bar(12,low=108,high=126,opening=110,close=120)])
    events=advance(store,policy,T+timedelta(minutes=13))
    assert [e['type'] for e in events]==['PAPER_ENTRY','PAPER_TARGET']
    assert store.plans()[0]['net_points']==pytest.approx(19.9)
    assert not advance(store,policy,T+timedelta(minutes=14))


def test_crossing_after_context_export_cannot_arm(store,policy):
    j,review=valid_job_and_review(store,policy)
    store.ingest([bar(10,high=108,observed=T+timedelta(minutes=10,seconds=10))])
    with pytest.raises(ValueError,match='crossed'):submit(store,review,policy,T+timedelta(minutes=10,seconds=15))
    assert not store.plans()
    assert store.db.execute('SELECT count(*) FROM decisions').fetchone()[0]==0


def test_new_assignment_does_not_change_original_open_protection(store,policy):
    _,review=valid_job_and_review(store,policy)
    submit(store,review,policy,T+timedelta(minutes=10,seconds=10))
    original=store.plans()[0]
    assign(store,'claude')
    assert store.plans()[0]==original


def test_backup_restores_authoritative_paper_state(store,policy,tmp_path):
    _,review=valid_job_and_review(store,policy)
    submit(store,review,policy,T+timedelta(minutes=10,seconds=10))
    dest=tmp_path/'copy.sqlite3'
    store.backup(dest)
    copy=Store(dest)
    try:
        assert copy.plans()==store.plans()
        assert copy.state('processor')==store.state('processor')
    finally:copy.close()


def test_processed_source_correction_freezes_active_plan(store,policy):
    _,review=valid_job_and_review(store,policy)
    submit(store,review,policy,T+timedelta(minutes=10,seconds=10))
    store.ingest([bar(11,low=100,high=108,opening=102,close=107)])
    advance(store,policy,T+timedelta(minutes=12))
    assert store.plans(True)[0]['status']=='OPEN'
    store.ingest([bar(11,low=96,high=108,opening=102,close=107,observed=T+timedelta(minutes=13))])
    assert store.plans(True)[0]['status']=='REVIEW_REQUIRED'
    assert store.plans(True)[0]['stop']==97


def test_missing_minute_after_fill_does_not_fake_exit(store,policy):
    _,review=valid_job_and_review(store,policy)
    submit(store,review,policy,T+timedelta(minutes=10,seconds=10))
    store.ingest([bar(11,low=100,high=108,opening=102,close=107),bar(13,low=108,high=126,opening=110,close=120)])
    events=advance(store,policy,T+timedelta(minutes=14))
    assert events[-1]['type']=='MISSING_MINUTE_DURING_PLAN'
    assert store.plans(True)[0]['status']=='REVIEW_REQUIRED'
    assert 'exit_price' not in store.plans(True)[0]


def test_known_gap_stop_precedes_later_range_ambiguity(store,policy):
    p={'id':'p','instrument':'NIFTY','status':'OPEN','direction':'LONG','entry':100,'fill_price':100,
       'stop':90,'target':120,'created_at':T.isoformat(),'expires_at':(T+timedelta(minutes=10)).isoformat()}
    with store.db:store.save_plan(p)
    store.ingest([bar(0,low=84,high=125,opening=85,close=100)])
    events=advance(store,policy,T+timedelta(minutes=1))
    assert events[0]['type']=='PAPER_STOP' and store.plans()[0]['exit_price']==85
