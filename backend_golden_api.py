from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class GoldenModel(BaseModel):
    athlete_id: str
    model_data: dict

@app.post("/api/golden-model/")
def upload_golden_model(payload: GoldenModel):
    print(f"Golden model uploaded for athlete {payload.athlete_id}")
    return {"status": "success"}

@app.get("/api/ping")
def ping():
    return {"status": "golden-api-alive"}
