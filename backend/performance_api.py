from fastapi import APIRouter
import time

router = APIRouter(prefix="/api/performance", tags=["performance"])

@router.get("/")
def performance():
    return {"uptime": "OK", "metrics": {}}
