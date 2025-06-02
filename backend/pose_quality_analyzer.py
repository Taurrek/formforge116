# backend/pose_quality_analyzer.py
import numpy as np

def score_pose_frame(keypoints):
    if keypoints is None or len(keypoints) == 0:
        return 0

    angles = compute_joint_angles(keypoints)
    stability = compute_variability(keypoints)

    biomech_score = biomechanical_plausibility(angles)
    stability_score = 1 - min(stability, 1.0)

    return round((biomech_score + stability_score) / 2, 2)

def compute_joint_angles(keypoints):
    # Example: angle at knee or elbow
    def angle(p1, p2, p3):
        v1 = np.array(p1) - np.array(p2)
        v2 = np.array(p3) - np.array(p2)
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2) + 1e-6)
        return np.degrees(np.arccos(np.clip(cos_angle, -1.0, 1.0)))

    try:
        knee_angle = angle(keypoints[11], keypoints[13], keypoints[15])
        return {'knee_angle': knee_angle}
    except:
        return {}

def compute_variability(keypoints):
    # Placeholder: return high variability if keypoints jitter
    coords = np.array(keypoints)
    return np.std(coords)

def biomechanical_plausibility(angles):
    if not angles:
        return 0
    angle_val = angles.get('knee_angle', 90)
    if 60 <= angle_val <= 160:
        return 1.0
    elif 40 <= angle_val <= 180:
        return 0.7
    return 0.3
