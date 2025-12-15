import time
from fastapi import WebSocket
from app.database import create_session, log_event
from app.llm import stream_llm

async def session_socket(websocket: WebSocket, session_id: str):
    await websocket.accept()
    start_time = time.time()

    await create_session(session_id)
    messages = [{"role": "system", "content": "You are a helpful assistant."}]

    try:
        while True:
            user_input = await websocket.receive_text()
            messages.append({"role": "user", "content": user_input})
            await log_event(session_id, "user_message", user_input)
            await stream_llm(session_id, messages, websocket)

    except Exception:
        duration = int(time.time() - start_time)
        print(f"Session {session_id} ended after {duration}s")
