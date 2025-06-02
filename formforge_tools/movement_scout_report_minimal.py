import json
import sys

def generate_sample_scouting_report(session_folder):
    landmark_file = f"{session_folder}/output_landmarks.json"
    
    with open(landmark_file, 'r') as f:
        landmarks = json.load(f)
    
    if not landmarks or not landmarks[0]['pose']:
        report = "Insufficient keypoint data for scouting report."
    else:
        first_frame = landmarks[0]['pose']
        # Example analysis (for illustration only)
        left_foot = first_frame[15]  # landmark index 15 (left ankle)
        right_foot = first_frame[16] # landmark index 16 (right ankle)
        left_hand = first_frame[11]  # left wrist
        right_hand = first_frame[12] # right wrist
        
        # Generate detailed narrative in layman's terms
        report = (
            f"Scouting Report - Frame 0:\n"
            f"The athlete's left foot is positioned at coordinates {left_foot}, "
            f"while the right foot is at {right_foot}. This indicates a stable base.\n"
            f"The left hand is at {left_hand} and the right hand at {right_hand}, "
            f"suggesting the athlete is preparing for an action with upper body engagement.\n"
            f"Further detailed biomechanical analysis can be developed here."
        )
    
    report_file = f"{session_folder}/scouting_report.txt"
    with open(report_file, 'w') as f:
        f.write(report)
    
    print(f"Scouting report saved to: {report_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 movement_scout_report_minimal.py <session_folder>")
        sys.exit(1)
    generate_sample_scouting_report(sys.argv[1])
