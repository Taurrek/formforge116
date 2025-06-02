# formforge/day01_to_21/formforge_day01_keypoints.py

import cv2
import numpy as np
from cvzone.PoseModule import PoseDetector

def extract_keypoints(video_path):
    print("[day01] Extracting keypoints using cvzone + MediaPipe...")

    cap = cv2.VideoCapture(video_path)
    detector = PoseDetector()
    keypoints = []

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = detector.findPose(frame)
        lm_list, _ = detector.findPosition(frame)

        # Store x, y coordinates of all visible joints (landmarks)
        if lm_list:
            pose = np.array([[pt[1], pt[2]] for pt in lm_list], dtype=np.float32)
        else:
            pose = np.zeros((33, 2), dtype=np.float32)

        keypoints.append(pose)

    cap.release()
    keypoints = np.array(keypoints)
    return keypoints
