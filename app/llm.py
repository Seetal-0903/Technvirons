import json
from openai import AsyncOpenAI
from app.database import log_event

client = AsyncOpenAI()

TOOLS = [{
    "type": "function",
    "function": {
        "name": "fetch_internal_data",
        "description": "Simulated internal tool",
        "parameters": {
            "type": "object",
            "properties": {"query": {"type": "string"}}
        }
    }
}]

async def fetch_internal_data(query: str):
    return f"Internal data for: {query}"

async def stream_llm(session_id, messages, websocket):
    stream = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=TOOLS,
        stream=True
    )

    async for chunk in stream:
        delta = chunk.choices[0].delta

        if delta.tool_calls:
            args = json.loads(delta.tool_calls[0].function.arguments)
            result = await fetch_internal_data(args["query"])
            messages.append({"role": "tool", "content": result})
            await log_event(session_id, "tool_call", result)
            continue

        if delta.content:
            await websocket.send_text(delta.content)
            await log_event(session_id, "ai_token", delta.content)
