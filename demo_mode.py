import requests
import json
import time
import os

GOLDEN_API_URL = "http://127.0.0.1:8000/api/golden-model/"
AVATAR_STATE_PATH = "frontend/public/avatar_state.json"
SIM_OUTPUT_PATH = "output/sim_output.json"

def upload_sample_golden():
    payload = {
        "athlete_id": "golden_123",
        "model_data": {
            "sport": "Basketball",
            "position": "PointGuard",
            "joint_cluster": "UpperBody",
            "data": {
                "joint_1": 30.0,
                "joint_2": 45.5,
                "joint_3": 12.1
            }
        }
    }
    print("Uploading sample golden model...")
    resp = requests.post(GOLDEN_API_URL, json=payload)
    print("Upload response:", resp.json())

def run_simulation():
    print("Running Flaw-to-Strain simulator...")
    simulated_output = {
        "timestamp": time.time(),
        "fatigue_score": 0.42,
        "frame": {
            "joint_1": 29.2,
            "joint_2": 44.1,
            "joint_3": 13.5
        }
    }
    os.makedirs(os.path.dirname(SIM_OUTPUT_PATH), exist_ok=True)
    with open(SIM_OUTPUT_PATH, "w") as f:
        json.dump(simulated_output, f, indent=2)
    print(f"Simulation output written to {SIM_OUTPUT_PATH}")

def write_avatar_state():
    print("Writing avatar_state.json...")
    avatar_data = {
        "athlete": "Athlete_1",
        "status": "active",
        "joints": {
            "joint_1": 29.2,
            "joint_2": 44.1,
            "joint_3": 13.5
        },
        "fatigue": 0.42,
        "timestamp": time.time()
    }
    os.makedirs(os.path.dirname(AVATAR_STATE_PATH), exist_ok=True)
    with open(AVATAR_STATE_PATH, "w") as f:
        json.dump(avatar_data, f, indent=2)
    print(f"Avatar state written to {AVATAR_STATE_PATH}")

def main():
    upload_sample_golden()
    run_simulation()
    write_avatar_state()

if __name__ == "__main__":
    main()
