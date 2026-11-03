# TornadoUI

TornadoUI is an independent AI chat interface and multi-model interaction platform derived from Open WebUI v0.6.5.

## Upstream attribution

- Upstream: Open WebUI (https://github.com/open-webui/open-webui)
- Source version: v0.6.5 (commit 07d8460126a686de9a99e2662d06106e22c3f6b6)
- License: BSD-3-Clause (original copyright retained)

TornadoUI is not the official Open WebUI project.

## Features

- Multi-model chat (Ollama, OpenAI-compatible APIs)
- RAG and document retrieval
- Tools, functions, prompts, channels
- Admin settings and user management
- Provider connection diagnostics endpoint (`/api/v1/diagnostics`)

## Tech stack

- Frontend: SvelteKit, Vite, Tailwind CSS
- Backend: Python, FastAPI, SQLAlchemy/SQLite/Postgres
- Realtime: Socket.IO

## Installation

### Backend

```bash
cd backend
python -m pip install -r requirements.txt
cd open_webui
python -m open_webui.main  # or uvicorn entrypoint per upstream docs
```

### Frontend

```bash
npm install
npm run dev
```

## Testing

```bash
cd backend/open_webui
PYTHONPATH=.. python -m pytest test/util/test_diagnostics.py
npm run test:frontend
npm run check
```

## Security notes

- Preserve original copyright notices (BSD-3-Clause).
- Secrets via environment variables; see `.env.example`.
- Admin-only diagnostics endpoint.

## License

BSD-3-Clause. See `LICENSE` and `THIRD_PARTY_NOTICES.md`.
