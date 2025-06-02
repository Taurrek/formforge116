def process_landmarks(landmark_data, sport, motion):
    summary = f"Landmark analysis for {motion} in {sport}:\n"

    if not landmark_data:
        return summary + "No landmark data available."

    try:
        if isinstance(landmark_data, list):
            summary += f"- {len(landmark_data)} frames of landmark data detected.\n"
        elif isinstance(landmark_data, dict):
            summary += f"- {len(landmark_data.keys())} body parts or categories detected.\n"
        else:
            summary += "- Unrecognized landmark data format.\n"
    except Exception as e:
        summary += f"Error processing landmarks: {str(e)}"

    # Placeholder: you can evolve this to compute asymmetry, angles, or key features
    summary += "- Further analysis coming soon.\n"

    return summary
