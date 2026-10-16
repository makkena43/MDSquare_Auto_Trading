"""One local authority: idempotent candles, immutable review jobs and paper events."""
import hashlib
import json
import sqlite3
from pathlib import Path
from mdsquare_trading.domain import Candle


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False)


def digest(value):
    return hashlib.sha256(canonical(value).encode()).hexdigest()


SCHEMA = '''
CREATE TABLE IF NOT EXISTS candles (
 id TEXT PRIMARY KEY, instrument TEXT NOT NULL, interval INTEGER NOT NULL,
 start TEXT NOT NULL, observed_at TEXT NOT NULL, payload TEXT NOT NULL);
CREATE INDEX IF NOT EXISTS candles_lookup ON candles(instrument, interval, start);
CREATE TABLE IF NOT EXISTS state (key TEXT PRIMARY KEY, payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS jobs (id TEXT PRIMARY KEY, payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS decisions (job_id TEXT PRIMARY KEY, payload TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS plans (id TEXT PRIMARY KEY, instrument TEXT NOT NULL, status TEXT NOT NULL, payload TEXT NOT NULL);
CREATE UNIQUE INDEX IF NOT EXISTS one_active_plan ON plans(instrument) WHERE status IN ('PENDING','OPEN','REVIEW_REQUIRED');
CREATE TABLE IF NOT EXISTS events (id TEXT PRIMARY KEY, payload TEXT NOT NULL);
'''


class Store:
    def __init__(self, path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.execute('PRAGMA foreign_keys=ON')
        self.db.executescript(SCHEMA)
        self.db.commit()

    def close(self):
        self.db.close()

    def state(self, key, default=None):
        row = self.db.execute('SELECT payload FROM state WHERE key=?', (key,)).fetchone()
        return json.loads(row[0]) if row else default

    def set_state(self, key, value):
        self.db.execute('INSERT INTO state VALUES (?,?) ON CONFLICT(key) DO UPDATE SET payload=excluded.payload',
                        (key, canonical(value)))

    def ingest(self, candles):
        with self.db:
            for bar in candles:
                row = self.db.execute('SELECT payload FROM candles WHERE id=?', (bar.id,)).fetchone()
                if row:
                    old = Candle.load(json.loads(row[0]))
                    # Repeated identical fetches preserve earliest observation; corrections get a new observation.
                    if (old.open, old.high, old.low, old.close) == (bar.open, bar.high, bar.low, bar.close):
                        continue
                    event = {'type': 'CANDLE_CORRECTION', 'bar_id': bar.id, 'old': old.record(), 'new': bar.record()}
                    self.event(event)
                    for plan in self.plans(active=True):
                        if plan['instrument'] == bar.instrument and plan.get('last_processed') and bar.start.isoformat() <= plan['last_processed'] and bar.end.isoformat() > plan['created_at']:
                            plan['status'] = 'REVIEW_REQUIRED'
                            plan['review_reason'] = 'Source revised an already-processed minute; no retroactive fill rewrite'
                            self.save_plan(plan)
                self.db.execute('INSERT INTO candles VALUES (?,?,?,?,?,?) ON CONFLICT(id) DO UPDATE SET observed_at=excluded.observed_at,payload=excluded.payload',
                                (bar.id, bar.instrument, bar.interval, bar.start.isoformat(), bar.observed_at.isoformat(), canonical(bar.record())))

    def candles(self, instrument, interval):
        return [Candle.load(json.loads(r[0])) for r in self.db.execute(
            'SELECT payload FROM candles WHERE instrument=? AND interval=? ORDER BY start', (instrument, interval))]

    def event(self, payload):
        key = digest(payload)
        self.db.execute('INSERT OR IGNORE INTO events VALUES (?,?)', (key, canonical(payload)))

    def plans(self, active=False):
        query = 'SELECT payload FROM plans'
        if active:
            query += " WHERE status IN ('PENDING','OPEN','REVIEW_REQUIRED')"
        return [json.loads(r[0]) for r in self.db.execute(query)]

    def save_plan(self, plan):
        self.db.execute('INSERT INTO plans VALUES (?,?,?,?) ON CONFLICT(id) DO UPDATE SET status=excluded.status,payload=excluded.payload',
                        (plan['id'], plan['instrument'], plan['status'], canonical(plan)))

    def save_job(self, job):
        with self.db:
            self.db.execute('INSERT OR IGNORE INTO jobs VALUES (?,?)', (job['context_id'], canonical(job)))

    def backup(self, path):
        destination = Path(path)
        if destination.exists():
            raise ValueError('Backup destination already exists')
        destination.parent.mkdir(parents=True, exist_ok=True)
        target = sqlite3.connect(path)
        try:
            self.db.backup(target)
        finally:
            target.close()
