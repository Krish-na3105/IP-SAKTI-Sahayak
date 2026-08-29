# IP-SAKTI Sahayak

AI-Powered Ayurvedic IP & Compliance Navigator — SIH 2026 V1 prototype.

## Quick start

### Backend
```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:3000.

Set `NEXT_PUBLIC_API_URL=http://localhost:8000` if needed.

Optional LLM support: set `OPENAI_API_KEY` and `OPENAI_MODEL` in `backend/.env`. The prototype remains functional without an API key using deterministic demo reasoning.

> Demo patent/TK data is synthetic and clearly labelled. Legal text is intentionally represented as curated metadata/demo guidance unless replaced with verified official source documents. Government fee values are stored in the backend data layer and should be verified against the latest official schedule before filing.
