from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/chart/{session_id}")
def get_chart(session_id: str):
    # Placeholder: use a static chart image for now
    chart_path = "backend/static/sample_chart.png"
    if os.path.exists(chart_path):
        return FileResponse(chart_path, media_type="image/png")
    return {"error": "Chart not found"}
