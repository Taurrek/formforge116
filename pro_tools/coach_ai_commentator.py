# injury_risk_predictor.py
import mediapipe as mp
import cv2
import numpy as np

def run_injury_risk(video_path):
    # your existing code here, adapted to function
    # save output video path or return analysis dict
    return {"status": "success", "message": "Injury risk analyzed"}

# Coach AI Commentator - Provides verbal feedback & analysis based on detected movements

mp_pose = mp.solutions.pose

def get_feedback(angles):
    feedback = []
    # Example feedback logic
    if angles.get('left_knee', 180) < 40:
        feedback.append("Bend your left knee a bit more for better shock absorption.")
    if angles.get('right_knee', 180) < 40:
        feedback.append("Bend your right knee a bit more for better shock absorption.")
    # Add more feedback rules as needed
    if not feedback:
        feedback.append("Great form! Keep it up!")
    return feedback

def calculate_joint_angles(landmarks):
    def angle_between(p1, p2, p3):
        a = np.array([p1.x, p1.y])
        b = np.array([p2.x, p2.y])
        c = np.array([p3.x, p3.y])
        ba = a - b
        bc = c - b
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.arccos(np.clip(cosine_angle, -1.0, 1.0))
        return np.degrees(angle)

    angles = {}
    angles['left_knee'] = angle_between(landmarks[mp_pose.PoseLandmark.LEFT_HIP],
                                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE],
                                        landmarks[mp_pose.PoseLandmark.LEFT_ANKLE])
    angles['right_knee'] = angle_between(landmarks[mp_pose.PoseLandmark.RIGHT_HIP],
                                         landmarks[mp_pose.PoseLandmark.RIGHT_KNEE],
                                         landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE])
    return angles

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark
                angles = calculate_joint_angles(landmarks)
                feedback_list = get_feedback(angles)
                y0 = 30
                for i, feedback in enumerate(feedback_list):
                    cv2.putText(image, feedback, (10, y0 + i*30), cv2.FONT_HERSHEY_SIMPLEX,
                                0.7, (0, 255, 255), 2)

            cv2.imshow('Coach AI Commentator', image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python coach_ai_commentator.py <video_path>")
        sys.exit(1)
    main(sys.argv[1])
