from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

class AuthData(BaseModel):
    username: str
    password: str

router = APIRouter(prefix="/api/auth", tags=["auth"])

@router.post("/register")
def register(data: AuthData):
    return {"detail": "registered"}

@router.post("")   # <- no slash here, so POST /api/auth works directly
def login(data: AuthData):
    return {"access_token": data.username, "token_type": "bearer"}
