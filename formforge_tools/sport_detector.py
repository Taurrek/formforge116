class SportDetector:
    def __init__(self):
        self.motion_patterns = {
            "baseball_swing": self.is_baseball_swing,
            "soccer_kick": self.is_soccer_kick,
            "tennis_serve": self.is_tennis_serve,
            "basketball_shot": self.is_basketball_shot,
            "running": self.is_running_motion,
        }

    def detect(self, pose_data):
        # If pose_data is a list, use the first valid pose dict
        if isinstance(pose_data, list) and len(pose_data) > 0:
            pose = pose_data[0]
        elif isinstance(pose_data, dict):
            pose = pose_data
        else:
            return "Unknown", "Unknown"

        for motion, checker in self.motion_patterns.items():
            if checker(pose):
                sport = self.map_motion_to_sport(motion)
                return sport, motion

        return "Unknown", "Unknown"

    def is_baseball_swing(self, pose):
        keypoints = pose.get("keypoints", [])
        return len(keypoints) >= 10 and keypoints[2][0] > keypoints[3][0]

    def is_soccer_kick(self, pose):
        keypoints = pose.get("keypoints", [])
        return len(keypoints) >= 15 and abs(keypoints[14][1] - keypoints[10][1]) > 50

    def is_tennis_serve(self, pose):
        keypoints = pose.get("keypoints", [])
        return len(keypoints) >= 8 and keypoints[4][1] < keypoints[2][1]

    def is_basketball_shot(self, pose):
        keypoints = pose.get("keypoints", [])
        return len(keypoints) >= 8 and keypoints[4][1] < keypoints[6][1]

    def is_running_motion(self, pose):
        keypoints = pose.get("keypoints", [])
        return len(keypoints) >= 10 and abs(keypoints[8][0] - keypoints[9][0]) > 20

    def map_motion_to_sport(self, motion):
        mapping = {
            "baseball_swing": "Baseball",
            "soccer_kick": "Soccer",
            "tennis_serve": "Tennis",
            "basketball_shot": "Basketball",
            "running": "Athletics"
        }
        return mapping.get(motion, "Unknown")

_detector_instance = SportDetector()

def detect_sport_and_motion(pose_data):
    return _detector_instance.detect(pose_data)
