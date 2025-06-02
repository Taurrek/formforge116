import os
import sys
import json

def extract_motion_ranges(session_path):
    angle_path = os.path.join(session_path, "pose_angles.json")
    if not os.path.exists(angle_path):
        print(f"Angle data not found at {angle_path}")
        return

    with open(angle_path, "r") as f:
        angle_data = json.load(f)

    joint_ranges = {}

    for frame in angle_data:
        if "angle_data" not in frame:
            continue
        for joint, angle in frame["angle_data"].items():
            if joint not in joint_ranges:
                joint_ranges[joint] = {
                    "min": angle,
                    "max": angle
                }
            else:
                joint_ranges[joint]["min"] = min(joint_ranges[joint]["min"], angle)
                joint_ranges[joint]["max"] = max(joint_ranges[joint]["max"], angle)

    output_path = os.path.join(session_path, "motion_ranges.json")
    with open(output_path, "w") as f:
        json.dump(joint_ranges, f, indent=4)

    print(f"Motion ranges saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python extract_motion_ranges.py <session_path>")
        sys.exit(1)

    extract_motion_ranges(sys.argv[1])
