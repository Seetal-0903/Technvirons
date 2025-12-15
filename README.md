# Realtime AI Backend (WebSockets + Supabase)

This repository implements a **real-time conversational AI backend** using **FastAPI, WebSockets, Supabase, and LLM streaming**.

## Features
- WebSocket-based low-latency streaming
- LLM tool/function calling
- Conversation state management
- Supabase persistence (sessions + event logs)
- Async post-session summarization
- Minimal frontend for testing

## Setup

```bash
git clone <repo>
cd realtime-ai-backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Environment Variables
```bash
export SUPABASE_URL=...
export SUPABASE_SERVICE_KEY=...
export OPENAI_API_KEY=...
```

## Run
```bash
uvicorn app.main:app --reload
```

Open `frontend/index.html` in browser.

## Supabase Schema
See SQL in assignment solution.

## Evaluation Notes
This project demonstrates:
- WebSocket streaming
- Tool calling
- Async persistence
- Post-session automation
