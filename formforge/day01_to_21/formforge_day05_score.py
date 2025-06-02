import numpy as np

def score_keypoints(normalized_keypoints):
    """
    Stub: Calculate mean score per frame as mean of all coords.
    Returns an array of shape (num_frames,)
    """
    print("[day05] Scoring keypoints")
    # Mean across keypoints and coordinates per frame
    return normalized_keypoints.mean(axis=(1,2))
