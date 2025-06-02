import os
import json
import numpy as np

# Assuming your key functions from previous steps exist here or import them accordingly
# For simplicity, this script loads keypoints.npy from a test video, normalizes, scores, then saves results.

def load_keypoints(path):
    return np.load(path)

def normalize_keypoints(keypoints_np):
    # Example normalization: scale keypoints to [0,1] by dividing by max coordinate found
    max_val = np.max(keypoints_np)
    norm_keypoints = keypoints_np / max_val if max_val > 0 else keypoints_np
    return norm_keypoints

def score_motion(session_np, baseline_np):
    distances = np.linalg.norm(session_np - baseline_np, axis=2)
    mean_dist = np.mean(distances)
    score = max(0, 100 - mean_dist * 100)
    print(f"Motion score: {score:.2f}")
    return score

def main():
    # Setup paths - update session_id for each session you want to process
    session_id = "session1"
    base_dir = "sessions"
    session_path = os.path.join(base_dir, session_id)
    os.makedirs(session_path, exist_ok=True)

    keypoints_path = os.path.join(session_path, "keypoints.npy")
    baseline_path = os.path.join(base_dir, "baseline.npy")
    score_path = os.path.join(session_path, "score.json")
    norm_keypoints_path = os.path.join(session_path, "normalized_keypoints.npy")

    # Load session keypoints
    if not os.path.exists(keypoints_path):
        print(f"Missing keypoints file at {keypoints_path}")
        return
    keypoints_np = load_keypoints(keypoints_path)
    print(f"Loaded keypoints shape: {keypoints_np.shape}")

    # Normalize keypoints
    norm_keypoints = normalize_keypoints(keypoints_np)
    print(f"Normalized keypoints shape: {norm_keypoints.shape}")

    # Load or create baseline
    if os.path.exists(baseline_path):
        baseline_np = np.load(baseline_path)
        print(f"Loaded baseline shape: {baseline_np.shape}")
    else:
        baseline_np = norm_keypoints
        np.save(baseline_path, baseline_np)
        print("Baseline created and saved.")

    # Score motion
    score = score_motion(norm_keypoints, baseline_np)

    # Save results
    with open(score_path, "w") as f:
        json.dump({"motion_score": score}, f)
    np.save(norm_keypoints_path, norm_keypoints)
    print(f"Saved score to {score_path}")
    print(f"Saved normalized keypoints to {norm_keypoints_path}")

if __name__ == "__main__":
    main()
