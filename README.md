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
(or) created a .env file in the project root

## Run
```bash
uvicorn app.main:app --reload
```

Open `frontend/index.html` in browser.

## Supabase Schema
'''bash
-- Enable UUID generation
create extension if not exists "uuid-ossp";

-- Main session table
create table if not exists public.sessions (
  session_id text primary key,
  user_id text,
  start_time timestamptz default now(),
  end_time timestamptz,
  duration_seconds integer,
  summary text
);

-- Detailed event log table
create table if not exists public.session_events (
  id bigserial primary key,
  session_id text references public.sessions(session_id) on delete cascade,
  event_type text,
  content text,
  created_at timestamptz default now()
);
'''

## Evaluation Notes
This project demonstrates:
- WebSocket streaming
- Tool calling
- Async persistence
- Post-session automation
