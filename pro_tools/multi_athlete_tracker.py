# injury_risk_predictor.py
import mediapipe as mp
import cv2
import numpy as np

def run_injury_risk(video_path):
    # your existing code here, adapted to function
    # save output video path or return analysis dict
    return {"status": "success", "message": "Injury risk analyzed"}

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

class AthleteTracker:
    def __init__(self):
        self.athlete_count = 0
        self.tracks = {}

    def assign_id(self, landmark_list):
        # Naive assignment based on horizontal position for demo
        avg_x = np.mean([lm.x for lm in landmark_list])
        assigned_id = None
        for aid, track in self.tracks.items():
            if abs(track - avg_x) < 0.1:
                assigned_id = aid
                self.tracks[aid] = avg_x
                break
        if assigned_id is None:
            self.athlete_count += 1
            assigned_id = self.athlete_count
            self.tracks[assigned_id] = avg_x
        return assigned_id

def main(video_path):
    cap = cv2.VideoCapture(video_path)
    tracker = AthleteTracker()

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(image)
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            if results.pose_landmarks:
                # For demo, we treat single person as one athlete
                athlete_id = tracker.assign_id(results.pose_landmarks.landmark)
                mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
                cv2.putText(image, f"Athlete ID: {athlete_id}", (30, 30),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

            cv2.imshow("Multi-Athlete Tracker", image)
            if cv2.waitKey(10) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python multi_athlete_tracker.py <video_path>")
        sys.exit(1)
    main(sys.argv[1])
