# injury_risk_predictor.py
import mediapipe as mp
import cv2
import numpy as np

def run_injury_risk(video_path):
    # your existing code here, adapted to function
    # save output video path or return analysis dict
    return {"status": "success", "message": "Injury risk analyzed"}

mp_pose = mp.solutions.pose

def calculate_joint_angles(landmarks):
    # Example: Calculate knee angle
    def angle_between_points(a, b, c):
        a = np.array([a.x, a.y])
        b = np.array([b.x, b.y])
        c = np.array([c.x, c.y])
        ba = a - b
        bc = c - b
        cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
        angle = np.arccos(cosine_angle)
        return np.degrees(angle)

    angles = {}
    # Right knee angle example
    angles['right_knee'] = angle_between_points(
        landmarks[mp_pose.PoseLandmark.RIGHT_HIP],
        landmarks[mp_pose.PoseLandmark.RIGHT_KNEE],
        landmarks[mp_pose.PoseLandmark.RIGHT_ANKLE])
    # Add more joints as needed

    return angles

def get_feedback(angles):
    feedback = []
    # Example risk detection logic
    if 'right_knee' in angles:
        if angles['right_knee'] < 40:
            feedback.append("Warning: Right knee angle too acute, risk of injury!")
    # Add more feedback logic here

    return feedback

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
                    cv2.putText(image, feedback, (10, y0 + i * 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

            cv2.imshow('Coach AI Commentator', image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python injury_risk_predictor.py <video_path>")
        sys.exit(1)
    main(sys.argv[1])
