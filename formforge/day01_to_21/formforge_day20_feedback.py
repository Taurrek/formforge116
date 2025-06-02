import os
import numpy as np
import json

# === Day 20: User Feedback + Flag System ===

JOINT_NAMES = [
    "Nose", "Neck", "RShoulder", "RElbow", "RWrist",
    "LShoulder", "LElbow", "LWrist", "RHip", "RKnee",
    "RAnkle", "LHip", "LKnee", "LAnkle", "REye",
    "LEye", "REar", "LEar"
]

def load_normalized_keypoints(session_path):
    return np.load(os.path.join(session_path, "normalized_keypoints.npy"))

def load_baseline_keypoints():
    return np.load("sessions/session1/normalized_keypoints.npy")

def detect_flaws(session_kps, baseline_kps, threshold=0.1):
    flaws = []
    num_joints = session_kps.shape[1]
    for joint_idx in range(num_joints):
        deviation = np.mean(np.abs(session_kps[:, joint_idx, 0] - baseline_kps[:, joint_idx, 0]))  # X-axis
        if deviation > threshold:
            flaws.append({
                "joint": JOINT_NAMES[joint_idx],
                "type": "X-deviation",
                "deviation": round(float(deviation), 3)
            })
    return flaws

def generate_feedback(flaws):
    feedback = []
    for flaw in flaws:
        joint = flaw["joint"]
        deviation = flaw["deviation"]
        msg = f"{joint} is off by {deviation:.3f} (X-axis). Suggest correcting arm/leg alignment or posture."
        feedback.append(msg)
    return feedback

def save_feedback(session_path, flaws, feedback):
    flags = {
        "flaws": flaws,
        "feedback": feedback
    }
    out_path = os.path.join(session_path, "flags.json")
    with open(out_path, "w") as f:
        json.dump(flags, f, indent=2)
    print(f"Feedback and flags saved to {out_path}")

def analyze_session(session_path):
    print(f"\n=== Day 20: Feedback for {session_path} ===")
    try:
        session_kps = load_normalized_keypoints(session_path)
        baseline_kps = load_baseline_keypoints()
    except Exception as e:
        print(f"Failed to load data: {e}")
        return
    flaws = detect_flaws(session_kps, baseline_kps)
    if not flaws:
        print("✅ No flaws detected.")
        return
    feedback = generate_feedback(flaws)
    for f in feedback:
        print(f"• {f}")
    save_feedback(session_path, flaws, feedback)

if __name__ == "__main__":
    analyze_session("sessions/session2")
