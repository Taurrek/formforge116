import numpy as np
from scipy.spatial.distance import cdist
import os
from flask import jsonify

# 1. Enhanced Dynamic Time Warping (DTW) for alignment
def dynamic_time_warping(user_sequence, golden_sequence):
    len_user = len(user_sequence)
    len_golden = len(golden_sequence)
    dp = np.zeros((len_user, len_golden))
    
    dp[0, 0] = np.abs(user_sequence[0] - golden_sequence[0]).sum()
    
    for i in range(1, len_user):
        dp[i, 0] = np.abs(user_sequence[i] - golden_sequence[0]).sum() + dp[i - 1, 0]
    for j in range(1, len_golden):
        dp[0, j] = np.abs(user_sequence[0] - golden_sequence[j]).sum() + dp[0, j - 1]
    
    for i in range(1, len_user):
        for j in range(1, len_golden):
            cost = np.abs(user_sequence[i] - golden_sequence[j]).sum()
            dp[i, j] = min(dp[i - 1, j], dp[i, j - 1], dp[i - 1, j - 1]) + cost
    
    aligned_user_sequence = []
    aligned_golden_sequence = []
    
    i, j = len_user - 1, len_golden - 1
    while i >= 0 and j >= 0:
        aligned_user_sequence.append(user_sequence[i])
        aligned_golden_sequence.append(golden_sequence[j])
        if i > 0 and j > 0 and dp[i, j] == dp[i - 1, j - 1] + np.abs(user_sequence[i] - golden_sequence[j]).sum():
            i -= 1
            j -= 1
        elif i > 0 and dp[i, j] == dp[i - 1, j]:
            i -= 1
        else:
            j -= 1
    
    return np.array(aligned_user_sequence[::-1]), np.array(aligned_golden_sequence[::-1])

# 2. Calculate the Difference Map with MSE for joint deviations
def compute_difference_map(user_sequence, golden_sequence):
    aligned_user, aligned_golden = dynamic_time_warping(user_sequence, golden_sequence)
    diff_map = np.mean((aligned_user - aligned_golden) ** 2, axis=1)  # MSE per joint
    return diff_map

# 3. Dynamic Threshold Calculation based on data variability
def dynamic_threshold(diff_map):
    mean_error = np.mean(diff_map)
    std_dev = np.std(diff_map)
    threshold = mean_error + std_dev  # Dynamically adjusts based on data variation
    return threshold

# 4. Main Real-Time Inference Function to invoke above methods
def real_time_inference(request):
    golden_sequence = np.array(request.json['golden_sequence'])
    user_sequence = np.array(request.json['user_sequence'])

    diff_map = compute_difference_map(user_sequence, golden_sequence)
    threshold = dynamic_threshold(diff_map)

    major_flaws = [(i, error) for i, error in enumerate(diff_map) if error > threshold]

    render_overlay_video(user_sequence, golden_sequence, diff_map)
    
    # Export Flaw Report
    export_flaw_report(diff_map, threshold=threshold, out_path="output/feedback_report.json")

    return jsonify({
        "difference_map": diff_map.tolist(),
        "major_flaws": major_flaws
    }), 200

# 5. Visualization - Render video overlay based on differences
def render_overlay_video(user_sequence, golden_sequence, diff_map):
    h, w = 1080, 1920  # Default dimensions for video rendering
    canvas = np.zeros((h, w, 3), dtype=np.uint8)

    for i, (user_frame, golden_frame, error) in enumerate(zip(user_sequence, golden_sequence, diff_map)):
        user_pts = np.array(user_frame) * 300 + np.array([w // 2 + 150, h // 2])
        golden_pts = np.array(golden_frame) * 300 + np.array([w // 2 + 150, h // 2])

        color = (0, 255, 0)  # Default color (green for okay)
        if error > 0.2:
            color = (0, 0, 255)  # Red for significant flaws
        cv2.circle(canvas, (int(user_pts[0]), int(user_pts[1])), 4, color, -1)
        cv2.circle(canvas, (int(golden_pts[0]), int(golden_pts[1])), 4, (255, 0, 0), -1)

    cv2.imshow("Real-Time Overlay", canvas)
    cv2.waitKey(1)

# 6. Export flaw report to JSON
def export_flaw_report(diff_map, threshold=0.2, out_path="output/feedback_report.json"):
    report = []
    for i, frame_errors in enumerate(diff_map):
        flaws = [{"joint": int(j), "error": float(round(e, 4))} for j, e in enumerate(frame_errors) if e > threshold]
        if flaws:
            report.append({"frame": i, "flaws": flaws})

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(report, f, indent=4)

