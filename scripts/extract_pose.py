import cv2
import os
import sys
import json
import mediapipe as mp

# Import your data_manager functions if needed
from scripts import data_manager  # assuming your data_manager.py is inside scripts/

def extract_pose_from_video(video_path, session_name):
    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)
    
    # Prepare output directory for session
    session_path = os.path.join("sessions", session_name)
    os.makedirs(session_path, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Cannot open video {video_path}")
        return
    
    frame_num = 0
    pose_data_list = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert BGR to RGB for MediaPipe
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(image_rgb)

        if results.pose_landmarks:
            landmarks = []
            for lm in results.pose_landmarks.landmark:
                landmarks.append({"x": lm.x, "y": lm.y, "z": lm.z, "visibility": lm.visibility})
        else:
            landmarks = []

        # Save frame as JPG
        frame_filename = os.path.join(session_path, f"frame_{frame_num:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        # Save pose landmarks JSON
        json_filename = os.path.join(session_path, f"frame_{frame_num:04d}.json")
        with open(json_filename, 'w') as f:
            json.dump({"landmarks": landmarks}, f)

        pose_data_list.append({"frame": frame_num, "landmarks": landmarks})

        frame_num += 1

    cap.release()
    pose.close()

    # Save full pose data JSON summary for the session
    summary_json = os.path.join(session_path, f"{session_name}_pose_data.json")
    with open(summary_json, 'w') as f:
        json.dump(pose_data_list, f)

    print(f"Processed {frame_num} frames. Pose data saved to {summary_json}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python extract_pose.py <video_path> <session_name>")
        sys.exit(1)
    
    video_path = sys.argv[1]
    session_name = sys.argv[2]

    extract_pose_from_video(video_path, session_name)
