# formforge_tools/fatigue_detection.py

def detect_fatigue(pose_sequence):
    """
    Detect signs of fatigue based on pose changes over session.

    Args:
        pose_sequence (list): List of pose frames.

    Returns:
        dict: {
            "fatigue_level": float,
            "fatigue_signs": list,
            "recommendations": list
        }
    """
    fatigue_level = 0.45
    fatigue_signs = ["decreased joint angle range", "slower limb movement"]
    recommendations = ["Take 5 min rest", "Hydrate and stretch"]

    return {
        "fatigue_level": fatigue_level,
        "fatigue_signs": fatigue_signs,
        "recommendations": recommendations
    }

if __name__ == "__main__":
    dummy_sequence = [{}] * 40
    print(detect_fatigue(dummy_sequence))
