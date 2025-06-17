from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

GOLDEN_PATH = "golden_models/golden_model.json"

@app.post("/league/compare-golden")
async def compare_vs_golden(request: Request):
    body = await request.json()
    session_id = body.get("session_id", "")
    league_fatigue = 0.92  # fake avg for demo
    with open(GOLDEN_PATH) as f:
        golden = json.load(f)
    response = {
        "session_id": session_id,
        "golden_fatigue": golden.get("fatigue_baseline"),
        "league_avg_fatigue": league_fatigue,
        "delta": round(league_fatigue - golden.get("fatigue_baseline", 0), 2),
        "athletes": [
            {"athlete_id": "A1", "avg_fatigue": league_fatigue}
        ]
    }
    return response
