# session_comparator.py

import numpy as np
import json
from scipy.spatial.distance import euclidean
from fastapi import APIRouter, Query

router = APIRouter()

def load_keypoints(session_path):
    with open(session_path, 'r') as f:
        return json.load(f)['keypoints']

def compare_keypoints(kp1, kp2):
    diffs = []
    for i in range(min(len(kp1), len(kp2))):
        frame_diff = 0
        for j in range(len(kp1[i])):
            point1, point2 = kp1[i][j], kp2[i][j]
            if point1 and point2:
                frame_diff += euclidean(point1, point2)
        diffs.append(frame_diff)
    return diffs

@router.get("/compare_sessions")
def compare_sessions(session1: str = Query(...), session2: str = Query(...)):
    try:
        kps1 = load_keypoints(session1)
        kps2 = load_keypoints(session2)
        diffs = compare_keypoints(kps1, kps2)
        average_diff = round(np.mean(diffs), 3)
        feedback = "Very similar form" if average_diff < 10 else "Significant motion differences"

        return {
            "average_frame_difference": average_diff,
            "frame_differences": diffs,
            "insight": feedback
        }
    except Exception as e:
        return {"error": str(e)}
