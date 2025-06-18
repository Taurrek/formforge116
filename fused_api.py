from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import asyncio, requests
from datetime import datetime

app = FastAPI()

ALERT_URL = "http://localhost:8004/api/alert-condition"
HR_THRESHOLD = 82
VEL_THRESHOLD = 0.75

@app.websocket("/ws/fused-metrics")
async def ws_fused_metrics(ws: WebSocket):
    await ws.accept()
    try:
        while True:
            # generate one point per second
            now = datetime.utcnow().timestamp()
            point = {
                "timestamp": now,
                "joint_vel": 0.5 + (now % 5) * 0.1,
                "hr": 80 + int(now % 5)
            }
            await ws.send_json(point)

            # backend alerting
            if point["hr"] > HR_THRESHOLD:
                requests.post(
                    ALERT_URL,
                    json={"athlete_id":"A1","metric":"hr","value":point["hr"]},
                    timeout=1
                )
            if point["joint_vel"] > VEL_THRESHOLD:
                requests.post(
                    ALERT_URL,
                    json={"athlete_id":"A1","metric":"joint_vel","value":point["joint_vel"]},
                    timeout=1
                )

            await asyncio.sleep(1)
    except WebSocketDisconnect:
        return
