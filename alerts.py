from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

SLACK_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_CHANNEL = os.getenv("SLACK_CHANNEL", "#general")

client = WebClient(token=SLACK_TOKEN)

class Alert(BaseModel):
    athlete_id: str
    metric: str
    value: float

app = FastAPI()

def send_slack_message(text: str):
    try:
        client.chat_postMessage(channel=SLACK_CHANNEL, text=text)
    except SlackApiError as e:
        print(f"[ALERTS] Slack error: {e.response['error']}")

@app.post("/api/alert-condition")
async def alert_condition(alert: Alert, background_tasks: BackgroundTasks):
    text = f":rotating_light: *ALERT* → Athlete *{alert.athlete_id}* crossed *{alert.metric}* threshold: *{alert.value}*"
    background_tasks.add_task(send_slack_message, text)
    print(f"[ALERTS] queued Slack message: {text}")
    return {"status": "queued"}
