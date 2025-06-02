import os
import json
import numpy as np

def load_all_sessions(base_dir="sessions"):
    sessions = []
    if not os.path.exists(base_dir):
        print(f"No sessions directory found at {base_dir}")
        return sessions

    for session_id in sorted(os.listdir(base_dir)):
        session_path = os.path.join(base_dir, session_id)
        if not os.path.isdir(session_path):
            continue
        try:
            score_file = os.path.join(session_path, "score.json")
            with open(score_file, "r") as f:
                score_data = json.load(f)
            score = score_data.get("motion_score", None)

            keypoints = np.load(os.path.join(session_path, "keypoints.npy"))
            norm_keypoints = np.load(os.path.join(session_path, "normalized_keypoints.npy"))

            sessions.append({
                "session_id": session_id,
                "motion_score": score,
                "num_frames": keypoints.shape[0],
                "keypoints_shape": keypoints.shape,
                "norm_keypoints_shape": norm_keypoints.shape,
            })
        except Exception as e:
            print(f"Failed to load session {session_id}: {e}")
    return sessions

def print_summary(sessions):
    print(f"\nLoaded {len(sessions)} sessions.\n")
    for s in sessions:
        print(f"Session {s['session_id']}:")
        print(f"  Motion score: {s['motion_score']}")
        print(f"  Frames: {s['num_frames']}")
        print(f"  Keypoints shape: {s['keypoints_shape']}")
        print(f"  Normalized keypoints shape: {s['norm_keypoints_shape']}\n")

if __name__ == "__main__":
    sessions = load_all_sessions()
    print_summary(sessions)
