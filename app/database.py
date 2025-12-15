from supabase import create_client
import os

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_SERVICE_KEY")
)

async def create_session(session_id, user_id=None):
    supabase.table("sessions").insert({
        "session_id": session_id,
        "user_id": user_id
    }).execute()

async def log_event(session_id, event_type, content):
    supabase.table("session_events").insert({
        "session_id": session_id,
        "event_type": event_type,
        "content": content
    }).execute()

async def finalize_session(session_id, summary, duration):
    supabase.table("sessions").update({
        "summary": summary,
        "duration_seconds": duration
    }).eq("session_id", session_id).execute()
