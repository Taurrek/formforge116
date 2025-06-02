import os
import sys
import json
import math
from scripts.data_manager import DataManager

def calculate_angle(a, b, c):
    """Calculates the angle (in degrees) between three points a, b, c with b as the vertex."""
    def distance(p1, p2):
        return math.sqrt(sum((p1[k] - p2[k]) ** 2 for k in ['x', 'y', 'z']))
    
    ab = distance(a, b)
    bc = distance(b, c)
    ac = distance(a, c)
    
    try:
        angle_rad = math.acos((ab**2 + bc**2 - ac**2) / (2 * ab * bc))
        return math.degrees(angle_rad)
    except:
        return None

def analyze_session(session_path):
    dm = DataManager(session_path)
    dm.load_pose_data()
    angles_data = []

    for frame in dm.pose_data:
        landmarks = frame["landmarks"]
        if len(landmarks) < 33:
            continue

        # Left elbow angle (shoulder [11], elbow [13], wrist [15])
        left_elbow = calculate_angle(landmarks[11], landmarks[13], landmarks[15])
        # Right elbow angle (12, 14, 16)
        right_elbow = calculate_angle(landmarks[12], landmarks[14], landmarks[16])

        # Left knee angle (hip [23], knee [25], ankle [27])
        left_knee = calculate_angle(landmarks[23], landmarks[25], landmarks[27])
        # Right knee angle (24, 26, 28)
        right_knee = calculate_angle(landmarks[24], landmarks[26], landmarks[28])

        angles_data.append({
            "frame": frame["frame"],
            "left_elbow_angle": left_elbow,
            "right_elbow_angle": right_elbow,
            "left_knee_angle": left_knee,
            "right_knee_angle": right_knee
        })

    output_path = os.path.join(session_path, "pose_angles.json")
    with open(output_path, "w") as f:
        json.dump(angles_data, f, indent=2)

    print(f"Joint angles saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/analyze_pose.py <session_path>")
        sys.exit(1)

    analyze_session(sys.argv[1])
