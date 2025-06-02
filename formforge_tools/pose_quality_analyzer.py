def evaluate_pose_quality(keypoints):
    if not keypoints:
        return {"quality": "poor", "issues": ["No keypoints detected."]}

    angles = calculate_joint_angles(keypoints)
    smoothness = assess_motion_smoothness(keypoints)

    issues = []
    if any(a < 10 or a > 170 for a in angles.values()):
        issues.append("Unnatural joint angles detected.")
    if smoothness < 0.5:
        issues.append("Motion appears jerky.")

    return {
        "quality": "good" if not issues else "needs review",
        "issues": issues,
        "angles": angles,
        "smoothness": smoothness,
    }

def calculate_joint_angles(keypoints):  # Simplified
    return {"elbow": 90, "knee": 135}

def assess_motion_smoothness(keypoints):  # Placeholder
    return 0.8
