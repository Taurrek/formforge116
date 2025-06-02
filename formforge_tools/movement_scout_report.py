import os
import json

def analyze_pose_data(pose_data):
    if isinstance(pose_data, list) and pose_data:
        pose_data = pose_data[0]
    keypoints = pose_data.get("keypoints", [])

    if not keypoints or len(keypoints[0]) < 25:
        return "Insufficient keypoint data for scouting report."

    analysis = []

    # Extract rough features
    nose = keypoints[0][0]  # x-coordinate
    left_foot = keypoints[15]
    right_foot = keypoints[22]
    left_shoulder = keypoints[5]
    right_shoulder = keypoints[2]
    left_knee = keypoints[13]
    right_knee = keypoints[10]
    left_hip = keypoints[12]
    right_hip = keypoints[9]

    # Weight distribution
    foot_distance = abs(left_foot[0] - right_foot[0])
    shoulder_width = abs(left_shoulder[0] - right_shoulder[0])
    balance_shift = "even" if abs(left_foot[1] - right_foot[1]) < 20 else "left" if left_foot[1] > right_foot[1] else "right"

    analysis.append(f"- Athlete appears to begin with a {balance_shift}-weighted stance.")
    analysis.append(f"- Foot distance is {foot_distance:.1f}px, indicating a {'wide' if foot_distance > shoulder_width * 1.2 else 'standard'} base.")
    
    # Coiling or hip rotation
    hip_angle = abs(left_hip[0] - right_hip[0])
    if hip_angle > shoulder_width * 0.5:
        analysis.append("- Hips are engaged in a visible coiling motion suggesting rotational force buildup.")
    else:
        analysis.append("- Hips are relatively squared, indicating linear drive rather than rotation.")

    # Knee drive and leg lift
    knee_diff = abs(left_knee[1] - right_knee[1])
    if knee_diff > 40:
        analysis.append("- Significant leg lift detected during initiation, suggesting a drive or load phase.")

    # Posture lean
    posture = abs(left_shoulder[1] - right_shoulder[1])
    if posture > 30:
        lean_dir = "left" if left_shoulder[1] > right_shoulder[1] else "right"
        analysis.append(f"- Torso lean detected toward the {lean_dir} side, possibly for momentum or angle setup.")
    else:
        analysis.append("- Torso posture remains level during motion initiation.")

    # Final style
    style = "drop and drive" if knee_diff > 40 and hip_angle > 30 else "upright motion"
    analysis.append(f"- Movement style is consistent with a {style} pattern.")

    return "\n".join(analysis)

def generate_scout_report(session_path):
    pose_path = os.path.join(session_path, "pose_analysis_output.json")
    output_path = os.path.join(session_path, "scouting_report.txt")

    if not os.path.exists(pose_path):
        print(f"Pose data not found: {pose_path}")
        return

    with open(pose_path, "r") as f:
        pose_data = json.load(f)

    report = analyze_pose_data(pose_data)

    with open(output_path, "w") as out:
        out.write("=== SCOUTING REPORT ===\n\n")
        out.write(report)

    print(f"Scouting report saved to: {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 movement_scout_report.py <session_folder>")
    else:
        generate_scout_report(sys.argv[1])
