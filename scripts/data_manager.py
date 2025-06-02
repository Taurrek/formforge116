import json
import os
import matplotlib.pyplot as plt

class DataManager:
    def __init__(self, session_path):
        self.session_path = session_path
        self.pose_data = []

    def load_pose_data(self):
        pose_file = os.path.join(self.session_path, f"{os.path.basename(self.session_path)}_pose_data.json")
        if not os.path.exists(pose_file):
            raise FileNotFoundError(f"Pose file not found: {pose_file}")
        with open(pose_file, "r") as f:
            self.pose_data = json.load(f)

    def get_frame_pose(self, frame_number):
        for frame in self.pose_data:
            if frame["frame"] == frame_number:
                return frame
        return None

def visualize_frame(session_path, frame_number):
    dm = DataManager(session_path)
    dm.load_pose_data()
    frame_data = dm.get_frame_pose(frame_number)
    if not frame_data:
        print(f"Frame {frame_number} not found.")
        return

    landmarks = frame_data["landmarks"]
    x = [lm["x"] for lm in landmarks]
    y = [1 - lm["y"] for lm in landmarks]  # Flip y for visual alignment

    plt.figure(figsize=(6, 6))
    plt.scatter(x, y, c='red')
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi, yi, str(i), fontsize=8)
    plt.title(f"Pose Landmarks - Frame {frame_number}")
    plt.axis('equal')
    plt.grid(True)
    plt.show()
