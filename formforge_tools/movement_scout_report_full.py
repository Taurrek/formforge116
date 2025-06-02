import sys
import json
import os

def safe_get(landmarks, idx):
    if idx < len(landmarks):
        return landmarks[idx]
    else:
        return None

def vector_to_str(vec):
    if vec is None:
        return "Data unavailable"
    return f"[{vec[0]:.3f}, {vec[1]:.3f}, {vec[2]:.3f}]"

def generate_scouting_report(session_folder):
    landmarks_file = os.path.join(session_folder, "output_landmarks.json")
    report_file = os.path.join(session_folder, "scouting_report.txt")

    if not os.path.exists(landmarks_file):
        print(f"Landmarks file not found: {landmarks_file}")
        return

    with open(landmarks_file, "r") as f:
        data = json.load(f)

    if not data or "pose" not in data[0]:
        print("No pose data found in landmarks.")
        return

    report = "=== SCOUTING REPORT ===\n\n"

    for i, frame_data in enumerate(data):
        landmarks = frame_data.get("pose", [])
        if not landmarks:
            report += f"Frame {i}: No landmark data available.\n\n"
            continue

        left_foot = safe_get(landmarks, 15)
        right_foot = safe_get(landmarks, 16)
        left_hand = safe_get(landmarks, 11)
        right_hand = safe_get(landmarks, 12)
        head = safe_get(landmarks, 0)  # nose or head landmark

        report += f"Scouting Report - Frame {i}:\n"
        report += f"  Head position: {vector_to_str(head)}\n"
        report += f"  Left foot position: {vector_to_str(left_foot)}\n"
        report += f"  Right foot position: {vector_to_str(right_foot)}\n"

        if left_foot and right_foot:
            report += "  Base stance appears stable.\n"
        else:
            report += "  Base stance data incomplete.\n"

        report += f"  Left hand position: {vector_to_str(left_hand)}\n"
        report += f"  Right hand position: {vector_to_str(right_hand)}\n"

        if left_hand and right_hand:
            report += "  Upper body engagement looks balanced.\n"
        else:
            report += "  Upper body engagement data incomplete.\n"

        report += "\n"

    with open(report_file, "w") as f:
        f.write(report)

    print(f"Scouting report saved to: {report_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 movement_scout_report_full.py <session_folder>")
        sys.exit(1)
    generate_scouting_report(sys.argv[1])
