# backend/trainer_dashboard_api.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from database import get_session_by_id, save_trainer_notes

router = APIRouter()

class TrainerNote(BaseModel):
    session_id: str
    notes: str
    recommendations: list[str]
    priority: int  # 0-3

@router.post("/trainer/notes")
def add_note(note: TrainerNote):
    session = get_session_by_id(note.session_id)
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    save_trainer_notes(
        session_id=note.session_id,
        notes=note.notes,
        recommendations=note.recommendations,
        priority=note.priority,
    )
    return {"success": True, "msg": "Note saved"}
