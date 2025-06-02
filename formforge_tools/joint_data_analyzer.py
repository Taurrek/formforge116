import os
import pandas as pd

def analyze_joint_data(joint_csv_path, sport, motion, session_path):
    summary = f"Joint data analysis for {motion} in {sport}:\n"

    if not os.path.exists(joint_csv_path):
        return summary + "No joint data found.", []

    try:
        df = pd.read_csv(joint_csv_path)
        if df.empty:
            return summary + "Joint CSV file is empty.", []

        # Basic metrics
        joints = df.columns[1:]  # skip frame/time column
        for joint in joints:
            values = df[joint]
            summary += f"- {joint}: mean={values.mean():.2f}, max={values.max():.2f}, min={values.min():.2f}\n"

    except Exception as e:
        summary += f"Error reading joint data: {str(e)}\n"

    # Load optional chart images
    chart_dir = os.path.join(session_path, "joint_charts")
    if os.path.isdir(chart_dir):
        images = [os.path.join(chart_dir, f) for f in os.listdir(chart_dir) if f.endswith(('.png', '.jpg'))]
    else:
        images = []

    return summary, images
