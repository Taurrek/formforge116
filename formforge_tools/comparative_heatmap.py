# comparative_heatmap.py

import numpy as np
import matplotlib.pyplot as plt
import json
from fastapi import APIRouter, Query
from io import BytesIO
import base64

router = APIRouter()

def load_keypoints(session_path):
    with open(session_path, 'r') as f:
        return json.load(f)['keypoints']

def calculate_joint_usage(kps):
    usage = np.zeros(len(kps[0]))
    for frame in kps:
        for i, joint in enumerate(frame):
            if joint is not None:
                usage[i] += 1
    return usage / len(kps)

@router.get("/heatmap_compare")
def heatmap_compare(session1: str = Query(...), session2: str = Query(...)):
    kps1 = load_keypoints(session1)
    kps2 = load_keypoints(session2)

    usage1 = calculate_joint_usage(kps1)
    usage2 = calculate_joint_usage(kps2)

    diff = usage1 - usage2
    joints = range(len(usage1))

    plt.figure(figsize=(10, 5))
    plt.bar(joints, diff, color=['red' if d < 0 else 'green' for d in diff])
    plt.title("Joint Usage Difference (Session1 - Session2)")
    plt.xlabel("Joint Index")
    plt.ylabel("Normalized Usage Difference")

    buf = BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('utf-8')
    plt.close()

    imbalance_flag = "Left side dominant" if np.sum(diff[:len(diff)//2]) > np.sum(diff[len(diff)//2:]) else "Right side dominant"

    return {
        "heatmap_image": f"data:image/png;base64,{img_base64}",
        "imbalance_flag": imbalance_flag,
        "usage_diff": diff.tolist(),
    }
