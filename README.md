# Back-py

A small Flask JSON API used to practise CI/CD on Azure App Service.

## Endpoints

| Route | Returns |
|---|---|
| `GET /` | Service name, version, greeting |
| `GET /health` | `{"status": "ok"}` |
| `GET /api/greet/<name>` | `{"greeting": "Hello, <name>!"}` |
| `GET /api/sum?a=2&b=3` | `{"a": 2, "b": 3, "sum": 5}` (400 if either is not an integer) |

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
python app.py                    # http://127.0.0.1:8000
```

## Test and lint

```bash
pytest
ruff check .
```
