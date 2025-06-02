def classify_sport(pose_data):
    """
    Input: pose_data (list/dict of keypoints over time)
    Output: string sport name, e.g., "baseball_throw"
    Logic: ML model or rule-based heuristic
    """

    # Simplified heuristic example: check keypose patterns or movement speed
    # Replace with your trained model or heuristic logic

    # For now, assuming pose_data contains relevant keypoints sequences
    if detect_baseball_throw_pattern(pose_data):
        return "baseball_throw"
    # Add other sports checks here

    return "unknown"

def detect_baseball_throw_pattern(pose_data):
    # Detect key patterns for baseball throw (e.g., arm cocking angle, stride)
    # Placeholder logic, improve based on your biomechanics knowledge
    return True  # Assume true for now
