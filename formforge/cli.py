import os
import sys
import argparse
import uuid
import shutil
import numpy as np

from formforge.day01_to_21 import (
    formforge_day01_keypoints,
    formforge_day03_normalize,
    formforge_day05_score,
)

def run_pipeline(video_path: str):
    if not os.path.isfile(video_path):
        print(f"[❌] Video not found: {video_path}")
        sys.exit(1)

    print(f"[▶] Starting analysis for: {video_path}")

    session_id = f"session_{uuid.uuid4().hex[:6]}"
    session_path = os.path.join("test_output", session_id)
    os.makedirs(session_path, exist_ok=True)

    shutil.copy(video_path, os.path.join(session_path, "input_video.mp4"))

    # Extract keypoints
    keypoints = formforge_day01_keypoints.extract_keypoints(video_path)
    keypoints_path = os.path.join(session_path, "keypoints.npy")
    np.save(keypoints_path, keypoints)
    print(f"Extracted {len(keypoints)} frames of keypoints to {keypoints_path}")

    # Normalize keypoints
    normalized_keypoints = formforge_day03_normalize.normalize_keypoints(keypoints)
    normalized_path = os.path.join(session_path, "keypoints_normalized.npy")
    np.save(normalized_path, normalized_keypoints)
    print(f"Saved normalized keypoints to {normalized_path}")

    # Score keypoints
    scores = formforge_day05_score.score_keypoints(normalized_keypoints)
    print(f"Calculated scores (per frame):\n{scores}")

def main():
    parser = argparse.ArgumentParser(description="FormForge CLI video processing")
    parser.add_argument("--video", required=True, help="Path to input video file")
    args = parser.parse_args()

    run_pipeline(args.video)

if __name__ == "__main__":
    main()
