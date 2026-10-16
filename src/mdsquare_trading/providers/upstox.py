"""Upstox V3 GET adapter adapted from Quant Investing authentication/ingestion."""
import os
import time
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import quote
import requests
from mdsquare_trading.domain import Candle, INSTRUMENTS, IST


class MarketDataError(RuntimeError):
    pass


def access_token(legacy_config=None):
    token = os.environ.get('UPSTOX_ACCESS_TOKEN')
    if not token and legacy_config:
        import yaml
        with Path(legacy_config).open() as stream:
            config = yaml.safe_load(stream)
        if not isinstance(config, dict):
            raise MarketDataError('Legacy config must be a mapping')
        token = (config.get('app') or {}).get('access_token') or (config.get('upstox') or {}).get('access_token')
    if not isinstance(token, str) or not token.strip():
        raise MarketDataError('Set UPSTOX_ACCESS_TOKEN or supply --legacy-config; never commit credentials')
    return token.strip()


class Upstox:
    BASE = 'https://api.upstox.com/v3'

    def __init__(self, token, session=None, sleep=time.sleep):
        self._token, self._session, self._sleep = token, session or requests.Session(), sleep

    def _get(self, path):
        for attempt in range(3):
            try:
                response = self._session.get(self.BASE + path, headers={
                    'Accept': 'application/json', 'Authorization': f'Bearer {self._token}'}, timeout=(5, 25),
                    allow_redirects=False)
            except requests.RequestException:
                if attempt == 2:
                    raise MarketDataError('Upstox connection failed; no response body/credentials logged') from None
                self._sleep(2 ** attempt)
                continue
            if response.status_code in (401, 403):
                raise MarketDataError('Upstox authentication/permission rejected; refresh your access token')
            if response.status_code == 429 or response.status_code >= 500:
                if attempt < 2:
                    self._sleep(min(30, 2 ** attempt))
                    continue
            if response.status_code != 200:
                raise MarketDataError(f'Upstox market-data request failed (HTTP {response.status_code})')
            try:
                data = response.json()
                if data.get('status') != 'success' or not isinstance(data['data']['candles'], list):
                    raise ValueError
                return data['data']['candles']
            except (ValueError, KeyError, TypeError, AttributeError):
                raise MarketDataError('Invalid Upstox candle response') from None
        raise MarketDataError('Upstox retry limit reached')

    def _candles(self, path, instrument, interval, observed_at):
        result = {}
        rows = self._get(path)
        observed_at = observed_at or datetime.now(IST)
        for row in rows:
            try:
                if not isinstance(row, list) or len(row) < 5:
                    raise ValueError
                bar = Candle(instrument, row[0], interval, *row[1:5], observed_at)
                if bar.id in result and result[bar.id] != bar:
                    raise ValueError
                result[bar.id] = bar
            except (ValueError, TypeError):
                raise MarketDataError('Invalid/conflicting Upstox candle; batch not stored') from None
        return sorted(result.values(), key=lambda b: b.start)

    def intraday(self, instrument, observed_at):
        key = quote(INSTRUMENTS[instrument], safe='')
        return self._candles(f'/historical-candle/intraday/{key}/minutes/1', instrument, 1, observed_at)

    def history(self, instrument, first, last, observed_at, daily=False):
        if first > last:
            raise ValueError('History dates reversed')
        key = quote(INSTRUMENTS[instrument], safe='')
        unit, interval = ('days', 1440) if daily else ('minutes', 1)
        result = []
        while first <= last:
            end = min(last, first + timedelta(days=6))
            result.extend(self._candles(f'/historical-candle/{key}/{unit}/1/{end}/{first}',
                                        instrument, interval, observed_at))
            first = end + timedelta(days=1)
        return result
