from fastapi import FastAPI, WebSocket
from app.websocket import session_socket

app = FastAPI()

@app.websocket("/ws/session/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await session_socket(websocket, session_id)
