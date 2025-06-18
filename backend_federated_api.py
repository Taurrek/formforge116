from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import json
import csv
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_DIR = "session_data"
os.makedirs(DATA_DIR, exist_ok=True)

class SessionScore(BaseModel):
    session_id: str
    athlete_id: str
    score: float

class FatigueEntry(BaseModel):
    session_id: str
    athlete_id: str
    fatigue: float
    timestamp: str

# --- In-Memory DB ---
scores_db = []
fatigue_db = []

@app.post("/session/score")
async def submit_score(score: SessionScore):
    scores_db.append(score.dict())
    return {"status": "score submitted"}

@app.post("/broadcast/fatigue")
async def log_fatigue(entry: FatigueEntry):
    fatigue_db.append(entry.dict())
    return {"status": "fatigue logged"}

@app.get("/session/leaderboard")
async def get_leaderboard(session_id: str):
    filtered = [s for s in scores_db if s["session_id"] == session_id]
    sorted_scores = sorted(filtered, key=lambda x: x["score"], reverse=True)
    for i, entry in enumerate(sorted_scores):
        entry["rank"] = i + 1
    return {"session_id": session_id, "leaderboard": sorted_scores}

@app.post("/league/compare-golden")
async def compare_vs_golden(request: Request):
    body = await request.json()
    session_id = body.get("session_id", "")
    league_fatigue = 0.92  # demo
    with open("golden_models/golden_model.json") as f:
        golden = json.load(f)
    return {
        "session_id": session_id,
        "golden_fatigue": golden.get("fatigue_baseline"),
        "league_avg_fatigue": league_fatigue,
        "delta": round(league_fatigue - golden.get("fatigue_baseline", 0), 2),
        "athletes": [{"athlete_id": "A1", "avg_fatigue": league_fatigue}]
    }

@app.post("/auto-coach")
async def auto_coach(request: Request):
    body = await request.json()
    session_id = body.get("session_id", "")
    recs = []
    for score in scores_db:
        if score["session_id"] != session_id:
            continue
        fatigue = next((f["fatigue"] for f in fatigue_db if f["athlete_id"] == score["athlete_id"]), None)
        notes = []
        if score["score"] >= 90:
            notes.append("Excellent performance — consider progression")
        elif score["score"] >= 80:
            notes.append("On track — maintain intensity")
        else:
            notes.append("Below threshold — focus on fundamentals")
        if fatigue is not None and fatigue > 0.8:
            notes.append("High fatigue — recommend reduced load")
        recs.append({
            "athlete_id": score["athlete_id"],
            "score": score["score"],
            "fatigue": fatigue,
            "recommendations": notes
        })
    return {"session_id": session_id, "coaching": recs}

@app.get("/export/csv")
async def export_csv(session_id: str):
    filepath = f"{DATA_DIR}/session_{session_id}.csv"
    with open(filepath, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Athlete ID", "Score", "Fatigue", "Timestamp"])
        for score in scores_db:
            if score["session_id"] != session_id:
                continue
            fatigue = next((f for f in fatigue_db if f["athlete_id"] == score["athlete_id"]), {})
            writer.writerow([
                score["athlete_id"],
                score["score"],
                fatigue.get("fatigue", ""),
                fatigue.get("timestamp", "")
            ])
    return {"status": "csv exported", "file": filepath}

@app.get("/export/json")
async def export_json(session_id: str):
    filtered_scores = [s for s in scores_db if s["session_id"] == session_id]
    filtered_fatigue = [f for f in fatigue_db if f["session_id"] == session_id]
    output = {
        "session_id": session_id,
        "scores": filtered_scores,
        "fatigue": filtered_fatigue
    }
    path = f"{DATA_DIR}/session_{session_id}.json"
    with open(path, "w") as f:
        json.dump(output, f, indent=2)
    return {"status": "json exported", "file": path}
