import os
import numpy as np
import json

def load_session(session_path):
    try:
        with open(os.path.join(session_path, "score.json"), "r") as f:
            score_data = json.load(f)
        norm_kps = np.load(os.path.join(session_path, "normalized_keypoints.npy"))
        return {
            "path": session_path,
            "score": score_data.get("motion_score", 0),
            "normalized_keypoints": norm_kps,
        }
    except Exception as e:
        print(f"Failed to load session at {session_path}: {e}")
        return None

def compare_to_baseline(session_np, baseline_np):
    # Compute per-joint average deviation
    deviations = np.linalg.norm(session_np - baseline_np, axis=2)  # (frames, joints)
    avg_deviation_per_joint = np.mean(deviations, axis=0)  # (joints,)
    return avg_deviation_per_joint

def detect_flaws(avg_deviation_per_joint, threshold=0.15):
    flaws = []
    for i, deviation in enumerate(avg_deviation_per_joint):
        if deviation > threshold:
            flaws.append((i, deviation))
    return flaws

def joint_name(index):
    names = [
        "Nose", "Neck", "RShoulder", "RElbow", "RWrist",
        "LShoulder", "LElbow", "LWrist", "MidHip", "RHip",
        "RKnee", "RAnkle", "LHip", "LKnee", "LAnkle",
        "REye", "LEye", "LEar"
    ]
    return names[index] if index < len(names) else f"Joint{index}"

# --- Run flaw detection on all sessions except baseline ---
def main():
    baseline_path = "sessions/session1/normalized_keypoints.npy"
    if not os.path.exists(baseline_path):
        print("Missing baseline keypoints.")
        return
    baseline_np = np.load(baseline_path)

    print("=== Day 18: Flaw Detection ===")

    for i in range(2, 6):  # Check session2 to session5 if they exist
        session_dir = f"sessions/session{i}"
        if not os.path.exists(session_dir):
            continue

        session = load_session(session_dir)
        if not session:
            continue

        print(f"\nAnalyzing {session_dir}...")
        avg_devs = compare_to_baseline(session["normalized_keypoints"], baseline_np)
        flaws = detect_flaws(avg_devs)

        if not flaws:
            print("✅ No significant flaws detected.")
        else:
            print("❌ Flaws detected:")
            for joint_idx, dev in flaws:
                print(f"  - {joint_name(joint_idx)} deviation: {dev:.3f}")

if __name__ == "__main__":
    main()
