import cv2
import numpy as np
import json
import argparse
import os

def generate_ghost_overlay(video_path, norm_keypoints_np, output_path):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error opening video {video_path}")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    skeleton_pairs = [
        (1,2), (1,5), (2,3), (3,4), (5,6), (6,7),
        (1,8), (8,9), (9,10), (1,11), (11,12), (12,13),
        (1,0), (0,14), (14,16), (0,15), (15,17)
    ]

    frame_idx = 0
    while True:
        ret, frame = cap.read()
        if not ret or frame_idx >= norm_keypoints_np.shape[0]:
            break

        keypoints = norm_keypoints_np[frame_idx]  # shape (18,2)

        # Draw keypoints
        for i, (x_norm, y_norm) in enumerate(keypoints):
            x = int(x_norm * width)
            y = int(y_norm * height)
            cv2.circle(frame, (x, y), 5, (0, 255, 0), -1)

        # Draw skeleton lines
        for (p1, p2) in skeleton_pairs:
            if keypoints[p1][0] == 0 or keypoints[p1][1] == 0 or keypoints[p2][0] == 0 or keypoints[p2][1] == 0:
                continue
            pt1 = (int(keypoints[p1][0] * width), int(keypoints[p1][1] * height))
            pt2 = (int(keypoints[p2][0] * width), int(keypoints[p2][1] * height))
            cv2.line(frame, pt1, pt2, (0, 255, 255), 2)

        out.write(frame)
        frame_idx += 1

    cap.release()
    out.release()
    print(f"Overlay video saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Generate ghost overlay video")
    parser.add_argument('--session', type=str, default='session1', help='Session folder name')
    args = parser.parse_args()

    session_path = f"sessions/{args.session}"
    video_path = os.path.join(session_path, 'input_video.mp4')
    norm_kps_path = os.path.join(session_path, 'normalized_keypoints.npy')
    output_path = os.path.join(session_path, 'ghost_overlay.mp4')

    if not os.path.exists(video_path):
        print(f"Input video not found: {video_path}")
        return

    if not os.path.exists(norm_kps_path):
        print(f"Normalized keypoints not found: {norm_kps_path}")
        return

    norm_keypoints_np = np.load(norm_kps_path)
    generate_ghost_overlay(video_path, norm_keypoints_np, output_path)

if __name__ == "__main__":
    main()
