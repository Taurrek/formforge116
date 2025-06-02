# formforge_tools/multi_athlete_tracker.py

import cv2
import mediapipe as mp
import numpy as np

def track_multiple_athletes_dummy(video_frames):
    """
    Dummy function to simulate multi-athlete tracking and stats.

    Args:
        video_frames (list): List of frames with multiple pose detections.

    Returns:
        dict: {
            "athlete_stats": dict of athlete_id -> stats,
            "interaction_alerts": list of alerts
        }
    """
    athlete_stats = {
        "athlete_1": {"speed": 6.5, "distance_covered": 200},
        "athlete_2": {"speed": 7.0, "distance_covered": 210}
    }
    interaction_alerts = ["Athlete_1 and Athlete_2 proximity warning"]

    return {"athlete_stats": athlete_stats, "interaction_alerts": interaction_alerts}


mp_pose = mp.solutions.pose

class MultiAthleteTracker:
    def __init__(self, max_num_athletes=4, min_detection_confidence=0.5):
        self.pose = mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            enable_segmentation=False,
            min_detection_confidence=min_detection_confidence,
            min_tracking_confidence=0.5)
        self.max_num_athletes = max_num_athletes
        self.current_ids = {}  # athlete_id -> last_known_landmarks

    def detect_and_track(self, frame):
        """
        Detect and track multiple athletes by splitting the frame horizontally.

        Args:
            frame (np.ndarray): Single video frame.

        Returns:
            list of dicts: Each dict contains:
                - 'id': athlete ID string
                - 'keypoints': list of (x,y,z) tuples normalized
                - 'bbox': bounding box (x, y, w, h) in pixel coords
        """
        height, width, _ = frame.shape
        athletes_data = []

        region_width = width // self.max_num_athletes
        for i in range(self.max_num_athletes):
            x_start = i * region_width
            roi = frame[:, x_start:x_start + region_width]

            # Mediapipe expects RGB images
            results = self.pose.process(cv2.cvtColor(roi, cv2.COLOR_BGR2RGB))
            if results.pose_landmarks:
                landmarks = results.pose_landmarks.landmark
                keypoints = [(lm.x, lm.y, lm.z) for lm in landmarks]

                # Estimate bounding box from landmarks
                xs = [lm.x for lm in landmarks]
                ys = [lm.y for lm in landmarks]
                min_x = min(xs) * region_width + x_start
                max_x = max(xs) * region_width + x_start
                min_y = min(ys) * height
                max_y = max(ys) * height

                bbox = (
                    int(min_x), int(min_y),
                    int(max_x - min_x), int(max_y - min_y)
                )

                athlete_id = f"athlete_{i+1}"
                self.current_ids[athlete_id] = keypoints
                athletes_data.append({
                    "id": athlete_id,
                    "keypoints": keypoints,
                    "bbox": bbox
                })

        return athletes_data

    def release(self):
        self.pose.close()


if __name__ == "__main__":
    # For quick test, can switch to dummy or real tracking.
    use_dummy = False

    if use_dummy:
        dummy_frames = [{}] * 30
        results = track_multiple_athletes_dummy(dummy_frames)
        print(results)
    else:
        cap = cv2.VideoCapture(0)
        tracker = MultiAthleteTracker()

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            athletes = tracker.detect_and_track(frame)
            for athlete in athletes:
                x, y, w, h = athlete['bbox']
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                for kp in athlete['keypoints']:
                    kp_x = int(kp[0] * frame.shape[1])
                    kp_y = int(kp[1] * frame.shape[0])
                    cv2.circle(frame, (kp_x, kp_y), 5, (0, 0, 255), -1)
                cv2.putText(frame, athlete['id'], (x + 5, y + 20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

            cv2.imshow('Multi-Athlete Tracker', frame)
            if cv2.waitKey(1) & 0xFF == 27:  # ESC key to quit
                break

        tracker.release()
        cap.release()
        cv2.destroyAllWindows()
