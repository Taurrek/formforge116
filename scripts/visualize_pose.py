import os
import json
import cv2
import matplotlib.pyplot as plt

def visualize_frame(session_path, frame_num):
    img_path = os.path.join(session_path, f"frame_{frame_num:04d}.jpg")
    json_path = os.path.join(session_path, f"frame_{frame_num:04d}.json")
    
    if not os.path.exists(img_path) or not os.path.exists(json_path):
        print(f"Missing files for frame {frame_num}")
        return
    
    image = cv2.imread(img_path)
    with open(json_path, 'r') as f:
        pose_data = json.load(f)

    # Draw keypoints (assuming normalized coords in pose_data['landmarks'])
    h, w, _ = image.shape
    for landmark in pose_data.get('landmarks', []):
        x, y = int(landmark['x'] * w), int(landmark['y'] * h)
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title(f"Frame {frame_num}")
    plt.axis('off')
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python visualize_pose.py <session_path> <frame_num>")
        exit(1)
    session_path = sys.argv[1]
    frame_num = int(sys.argv[2])
    visualize_frame(session_path, frame_num)
