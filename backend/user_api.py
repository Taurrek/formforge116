from fastapi import APIRouter, Header, HTTPException

router = APIRouter(prefix="/api/user", tags=["user"])

@router.get("/profile")
def profile(authorization: str = Header(...)):
    # strip off "Bearer "
    token = authorization.replace("Bearer ", "").strip()
    if not token:
        raise HTTPException(status_code=401, detail="Missing token")
    return {"email": token, "name": ""}
