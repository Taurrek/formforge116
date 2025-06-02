from fastapi import FastAPI
from feedback_engine import router as feedback_router
from chart_generator import router as chart_router

app = FastAPI()

app.include_router(feedback_router)
app.include_router(chart_router)
