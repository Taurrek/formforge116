from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

@app.get("/")
def root():
    return {"status": "avatar api active"}

@app.get("/autocoach/feedback")
def get_feedback():
    try:
        with open("output/coach_feedback.json", "r") as f:
            feedback = json.load(f)
        return {"status": "ok", "feedback": feedback}
    except FileNotFoundError:
        return {"status": "error", "message": "No feedback file found"}
