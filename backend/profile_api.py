from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict

router = APIRouter(prefix="/api/user", tags=["user"])
fake_profiles: Dict[str, Dict] = {}

class ProfileIn(BaseModel):
    email: str
    display_name: str
    notifications_enabled: bool

@router.get("/profile")
async def get_profile(email: str):
    profile = fake_profiles.get(email)
    if not profile:
        # Return default empty profile
        return {"email": email, "display_name": "", "notifications_enabled": True}
    return profile

@router.post("/profile")
async def set_profile(profile: ProfileIn):
    fake_profiles[profile.email] = profile.dict()
    return {"status": "ok", **profile.dict()}
