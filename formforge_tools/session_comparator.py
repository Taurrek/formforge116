import numpy as np

def compare_sessions(session1_data, session2_data):
    kp1 = np.array(session1_data["keypoints"])
    kp2 = np.array(session2_data["keypoints"])

    if kp1.shape != kp2.shape:
        return {"error": "Mismatched keypoint data shape"}

    diff = np.linalg.norm(kp1 - kp2, axis=-1).mean()
    return {"difference_score": float(diff), "verdict": "similar" if diff < 20 else "different"}
