# Proofline

A runnable vertical-slice prototype for turning private engineering work into a bounded, recruiter-readable proof pack without uploading source code. The browser demo uses explicit fictional fixtures; the FastAPI service implements the same deterministic assessment and is source-only, not publicly hosted.

## Run

Requires Node 24.22.2 and Python 3.12+.

```bash
npm ci
npm run typecheck && npm run test:e2e && npm run build
uv sync --project api --locked --dev
uv run --project api pytest api/tests
uv run --project api uvicorn api.main:app --reload
```

The static frontend works on GitHub Pages. The local API exposes `POST /proof-packs`; it does not ingest source code. Read [product](docs/PRODUCT.md), [architecture](docs/ARCHITECTURE.md), and [source notes](research/notes.md). All market numbers are source-report estimates, not validated demand.
