# MDSquare Auto Trading

An automatic trading system. The design spec is in [`docs/spec.md`](docs/spec.md).

## Layout

| Path | What goes there |
|---|---|
| `src/mdsquare_trading/` | The Python package |
| `tests/` | pytest tests |
| `db/migrations/` | Numbered SQL migrations |
| `docs/` | Design spec and notes |

## Setup

```
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest -q
```
