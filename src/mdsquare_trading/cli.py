"""Local/cloud-portable, paper-only command line entry point."""
import argparse
from datetime import date, datetime, timedelta
import json
import os
from pathlib import Path
import time
from mdsquare_trading.domain import INSTRUMENTS, IST, Candle
from mdsquare_trading.store import Store
from mdsquare_trading.providers.upstox import Upstox, access_token, MarketDataError
from mdsquare_trading.service import assign, context, submit
from mdsquare_trading.engine import advance


def write(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(value,indent=2,allow_nan=False)+'\n')
    temp.replace(path)


def main(argv=None):
    parser = argparse.ArgumentParser(description='MDSquare underlying paper research. No broker order functionality.')
    parser.add_argument('--db',default='data/trading.sqlite3')
    parser.add_argument('--policy',default='config/paper.json')
    parser.add_argument('--legacy-config',default=os.environ.get('UPSTOX_LEGACY_CONFIG'))
    sub = parser.add_subparsers(dest='command',required=True)
    sub.add_parser('init')
    p=sub.add_parser('assign');p.add_argument('processor')
    sub.add_parser('backfill')
    sub.add_parser('poll')
    p=sub.add_parser('run');p.add_argument('--seconds',type=int,default=60)
    p=sub.add_parser('import-candles');p.add_argument('file')
    p=sub.add_parser('export-context');p.add_argument('instrument',choices=INSTRUMENTS);p.add_argument('--out',required=True)
    p=sub.add_parser('export-history');p.add_argument('instrument',choices=INSTRUMENTS);p.add_argument('--start',required=True);p.add_argument('--end',required=True);p.add_argument('--out',required=True)
    p=sub.add_parser('submit');p.add_argument('file')
    p=sub.add_parser('backup');p.add_argument('file')
    sub.add_parser('events')
    args=parser.parse_args(argv)
    store=Store(args.db)
    try:
        policy=json.loads(Path(args.policy).read_text())
        if policy.get('mode') != 'PAPER_RESEARCH':
            raise ValueError('Only PAPER_RESEARCH mode is implemented')
        now=lambda:datetime.now(IST)
        if args.command=='init':
            print(json.dumps({'database':args.db,'mode':'PAPER_RESEARCH','live_orders_supported':False}))
        elif args.command=='assign':
            print(json.dumps(assign(store,args.processor)))
        elif args.command=='backup':
            store.backup(args.file);print('Database backup complete')
        elif args.command=='events':
            for row in store.db.execute('SELECT payload FROM events ORDER BY rowid'):
                print(row[0])
        elif args.command=='import-candles':
            bars=[Candle.load(b) for b in json.loads(Path(args.file).read_text())]
            store.ingest(bars);print(json.dumps({'stored':len(bars)}))
        elif args.command=='export-context':
            advance(store,policy,now())
            write(args.out,context(store,args.instrument,policy,now()))
            print(f'Context written to {args.out}')
        elif args.command=='export-history':
            from mdsquare_trading.domain import aggregate, timestamp
            first,last=timestamp(args.start),timestamp(args.end)
            cutoff=now()
            if first>last or last>cutoff:
                raise ValueError('History slice must be ordered and not in future')
            bars=aggregate(store.candles(args.instrument,1),cutoff,policy['settle_seconds'])
            write(args.out,{'instrument':args.instrument,'as_of':cutoff.isoformat(),'five_minute':[b.record() for b in bars if first<=b.start<last]})
            print(f'History slice written to {args.out}')
        elif args.command=='submit':
            review=json.loads(Path(args.file).read_text())
            advance(store,policy,now())
            print(json.dumps(submit(store,review,policy,now())))
        else:
            client=Upstox(access_token(args.legacy_config))
            if args.command=='backfill':
                for instrument in INSTRUMENTS:
                    today=now().date()
                    for daily,days in [(False,policy['history_calendar_days']),(True,policy['daily_calendar_days'])]:
                        bars=client.history(instrument,today-timedelta(days=days),today-timedelta(days=1),None,daily)
                        store.ingest(bars)
                        print(json.dumps({'instrument':instrument,'interval':'daily' if daily else 'minute','stored':len(bars)}))
            else:
                if args.command=='run' and args.seconds<60:
                    raise ValueError('Poll interval must be at least 60 seconds')
                while True:
                    for instrument in INSTRUMENTS:
                        try:
                            bars=client.intraday(instrument,None)
                            store.ingest(bars)
                            for event in advance(store,policy,now()):print(json.dumps(event),flush=True)
                            print(json.dumps({'instrument':instrument,'stored':len(bars),'mode':'PAPER_RESEARCH'}),flush=True)
                        except MarketDataError as error:
                            with store.db:store.event({'type':'DATA_ERROR','instrument':instrument,'at':now().isoformat(),'reason':str(error)})
                            raise
                    if args.command=='poll':break
                    time.sleep(args.seconds)
    except (ValueError,KeyError,TypeError,MarketDataError) as error:
        parser.exit(2,f'{type(error).__name__}: {error}\n')
    finally:
        store.close()
