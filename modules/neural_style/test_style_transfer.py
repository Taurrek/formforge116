import sys
import os
sys.path.append(os.path.abspath("."))

from utils.npy_loader import load_npy_sequence
from modules.neural_style.style_transfer import normalize_pose_sequence, align_sequences_dtw, compute_difference_map
from modules.neural_style.visualize import render_overlay_video

# Load raw sequences (frames, joints, 3)
golden_raw = load_npy_sequence("/home/cj2k4211/formforge_project/test_output/session_3681f0")
user_raw   = load_npy_sequence("/home/cj2k4211/formforge_project/test_output/session_05f5cb")

# Slice to (frames, joints, 2) → drop confidence scores
golden_seq = normalize_pose_sequence(golden_raw[:, :, :2])
user_seq   = normalize_pose_sequence(user_raw[:, :, :2])

# Align using DTW
golden_aligned, user_aligned = align_sequences_dtw(golden_seq, user_seq)

# Compute joint-wise difference map
diff_map = compute_difference_map(user_aligned, golden_aligned)

# Visualize overlay
render_overlay_video(user_aligned, golden_aligned, diff_map)

# === Export flaw report to JSON for frontend ===
from modules.neural_style.export_feedback import export_flaw_report
export_flaw_report(diff_map, threshold=0.2, out_path="output/feedback_report.json")
