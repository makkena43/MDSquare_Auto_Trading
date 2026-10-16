"""Validated, timezone-aware underlying price records."""
from dataclasses import asdict, dataclass
from datetime import datetime, time, timedelta
import math
from zoneinfo import ZoneInfo

IST = ZoneInfo('Asia/Kolkata')
INSTRUMENTS = {'NIFTY': 'NSE_INDEX|Nifty 50', 'BANKNIFTY': 'NSE_INDEX|Nifty Bank'}


def timestamp(value):
    result = datetime.fromisoformat(value) if isinstance(value, str) else value
    if not isinstance(result, datetime) or result.tzinfo is None:
        raise ValueError('Timezone-aware timestamp required')
    return result.astimezone(IST)


def number(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ValueError('Finite numeric price required')
    return float(value)


@dataclass(frozen=True)
class Candle:
    instrument: str
    start: datetime
    interval: int
    open: float
    high: float
    low: float
    close: float
    observed_at: datetime

    def __post_init__(self):
        if self.instrument not in INSTRUMENTS or self.interval not in (1, 5, 1440):
            raise ValueError('Unsupported instrument or interval')
        object.__setattr__(self, 'start', timestamp(self.start))
        object.__setattr__(self, 'observed_at', timestamp(self.observed_at))
        for key in ('open', 'high', 'low', 'close'):
            object.__setattr__(self, key, number(getattr(self, key)))
        if not 0 < self.low <= min(self.open, self.close) <= max(self.open, self.close) <= self.high:
            raise ValueError('Invalid OHLC geometry')
        if self.start.second or self.start.microsecond:
            raise ValueError('Candle must start on a minute boundary')

    @property
    def end(self):
        if self.interval == 1440:
            return datetime.combine(self.start.date(), time(15, 30), IST)
        return self.start + timedelta(minutes=self.interval)

    @property
    def id(self):
        return f'{self.instrument}:{self.interval}:{self.start.isoformat()}'

    def record(self):
        return {**asdict(self), 'start': self.start.isoformat(), 'observed_at': self.observed_at.isoformat(), 'id': self.id}

    @classmethod
    def load(cls, value):
        return cls(**{k: v for k, v in value.items() if k != 'id'})


def aggregate(minutes, as_of, settle_seconds=5):
    """Emit only complete 09:15-aligned five-minute bars; never fill gaps."""
    as_of = timestamp(as_of)
    groups, seen = {}, {}
    for bar in minutes:
        if bar.interval != 1:
            raise ValueError('Aggregation requires one-minute bars')
        if bar.id in seen and bar != seen[bar.id]:
            raise ValueError('Conflicting duplicate minute')
        seen[bar.id] = bar
        local = bar.start
        if local.weekday() >= 5 or not time(9, 15) <= local.time() < time(15, 30):
            continue
        if bar.end + timedelta(seconds=settle_seconds) > as_of or bar.observed_at > as_of:
            continue
        slot = local.replace(minute=local.minute - local.minute % 5)
        groups.setdefault((bar.instrument, slot), {})[local] = bar
    result = []
    for (instrument, slot), bars in sorted(groups.items()):
        ordered = [bars.get(slot + timedelta(minutes=i)) for i in range(5)]
        if any(b is None for b in ordered):
            continue
        result.append(Candle(instrument, slot, 5, ordered[0].open, max(b.high for b in ordered),
                             min(b.low for b in ordered), ordered[-1].close,
                             max(b.observed_at for b in ordered)))
    return result
