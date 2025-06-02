# formforge_tools/activity_classifier.py

def classify_activity(pose_sequence):
    """
    Classify sport/activity from pose sequence.

    Args:
        pose_sequence (list): List of keypoints per frame.

    Returns:
        str: Activity label.
    """
    # Placeholder heuristic classification
    return "baseball_throw"

if __name__ == "__main__":
    dummy_sequence = [{}] * 25
    print("Activity:", classify_activity(dummy_sequence))
