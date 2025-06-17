from fastapi import APIRouter, Depends, HTTPException
from .database import get_db  # your DB session provider
from sqlalchemy.orm import Session

router = APIRouter(prefix="/api/admin", tags=["admin"])

@router.get("/users")
def get_all_users(db: Session = Depends(get_db)):
    users = db.execute("SELECT id, email, name, created_at FROM users").fetchall()
    return [dict(u) for u in users]

@router.get("/performance")
def get_performance_report(db: Session = Depends(get_db)):
    records = db.execute("SELECT timestamp, value, athlete_id FROM performance").fetchall()
    return [dict(r) for r in records]
