from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio
from datetime import datetime

app = FastAPI()

CAMERAS = ["A1", "A2", "A3"]  # stub athlete IDs

@app.websocket("/ws/cam/{athlete_id}")
async def ws_cam(ws: WebSocket, athlete_id: str):
    await ws.accept()
    try:
        while True:
            now = datetime.utcnow().timestamp()
            data = {
                "timestamp": now,
                "pose_score": 0.8 + (now % 5) * 0.02,   # stub metric
                "fatigue": 0.1 + (now % 5) * 0.05       # stub metric
            }
            await ws.send_json(data)
            await asyncio.sleep(1)
    except WebSocketDisconnect:
        return
