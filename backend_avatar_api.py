from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True,
    allow_methods=["*"], allow_headers=["*"]
)

@app.get("/")
def root():
    return {"status": "avatar api active"}

@app.get("/autocoach")
def get_auto_coach_feedback():
    return {
        "comments": [
            {"tag": "Posture", "message": "Maintain upright torso during sprint."},
            {"tag": "Arm Drive", "message": "Pump arms straight front-to-back."},
            {"tag": "Knee Lift", "message": "Lift knees higher to increase stride efficiency."}
        ]
    }
