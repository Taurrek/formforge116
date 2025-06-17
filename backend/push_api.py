from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from expo_push_sdk import Expo, ExpoPushError

router = APIRouter(prefix="/api/push")

# In-memory store; swap for DB in production
registered_tokens = set()

class TokenBody(BaseModel):
    token: str

@router.post("/register")
async def register_token(body: TokenBody):
    registered_tokens.add(body.token)
    return {"status": "registered"}

class NotificationBody(BaseModel):
    title: str
    message: str

@router.post("/send")
async def send_notification(body: NotificationBody):
    expo = Expo()
    messages = [
        {"to": t, "sound": "default", "title": body.title, "body": body.message}
        for t in registered_tokens
    ]
    try:
        receipts = expo.send_push_notifications(messages)
    except ExpoPushError as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"receipts": receipts}
