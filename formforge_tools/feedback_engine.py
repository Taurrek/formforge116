from fastapi import APIRouter, Request
from pydantic import BaseModel

router = APIRouter()

feedback_db = {}  # Temporary storage for feedback and AI notes

class Feedback(BaseModel):
    feedback: str

@router.get("/feedback/{session_id}")
def get_feedback(session_id: str):
    return {"notes": feedback_db.get(session_id, "No notes available.")}

@router.post("/feedback/{session_id}")
def post_feedback(session_id: str, data: Feedback):
    feedback_db[session_id] = data.feedback
    return {"message": "Feedback stored"}
