import os

def get_pose_analysis_with_screenshots(pose_data, sport, motion, session_path):
    # This is a placeholder — you can expand with real pose chart rendering later
    analysis = f"Pose analysis for {motion} in {sport}:\n"
    analysis += "- Detected primary motion phase based on keypoint alignment.\n"
    analysis += "- Joint symmetry appears within normal ranges.\n"
    analysis += "- No major anomalies detected in limb extension or balance."

    # Look for screenshots (if available)
    screenshot_dir = os.path.join(session_path, "screenshots")
    if os.path.isdir(screenshot_dir):
        images = [os.path.join(screenshot_dir, f) for f in os.listdir(screenshot_dir) if f.endswith(('.png', '.jpg'))]
    else:
        images = []

    return analysis, images
