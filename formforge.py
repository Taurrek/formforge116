import numpy as np

# Example of the dynamic time warping function
def dynamic_time_warping(golden_sequence, user_sequence):
    """
    Compute the Dynamic Time Warping (DTW) distance between two sequences.
    """
    # A basic example, replace this with your actual DTW logic
    distance = 0
    for g, u in zip(golden_sequence, user_sequence):
        distance += np.linalg.norm(np.array(g) - np.array(u))
    return distance

# Example of the function to compute the difference map
def compute_difference_map(user_sequence, golden_sequence):
    """
    Compute the difference map between two sequences.
    """
    diff_map = []
    for user, golden in zip(user_sequence, golden_sequence):
        diff = np.linalg.norm(np.array(user) - np.array(golden))
        diff_map.append(diff)
    return diff_map

# Example of the export_flaw_report function
def export_flaw_report(diff_map, threshold=0.2, out_path="output/feedback_report.json"):
    """
    Export a JSON report for flaws based on a threshold.
    """
    import json
    import os

    report = []
    for i, frame_errors in enumerate(diff_map):
        flaws = [{"joint": int(j), "error": float(round(e, 4))} for j, e in enumerate(frame_errors) if e > threshold]
        if flaws:
            report.append({"frame": i, "flaws": flaws})

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(report, f, indent=4)

