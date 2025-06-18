import cv2
import numpy as np

def render_overlay_video(seq_user, seq_golden, diff_map, w=640, h=480, threshold=0.2):
    for i in range(len(seq_user)):
        canvas = np.ones((h, w, 3), dtype=np.uint8) * 255
        user_frame = seq_user[i]
        golden_frame = seq_golden[i]
        
        # Ensure diff_map is an iterable with correct shape
        errors = diff_map[i] if isinstance(diff_map[i], np.ndarray) else np.array([diff_map[i]])

        user_pts = np.array(user_frame) * 300 + np.array([w // 2 - 150, h // 2])
        golden_pts = np.array(golden_frame) * 300 + np.array([w // 2 + 150, h // 2])

        major_flaws = []

        # Iterate through points and errors
        for j, (u, g, e) in enumerate(zip(user_pts, golden_pts, errors)):
            if e > threshold:
                color = (0, 0, 255)  # Red = flaw
                major_flaws.append((j, round(e, 3)))
            else:
                color = (0, 255, 0)  # Green = okay

            # Ensure u and g are tuples of integers and correctly plot them
            cv2.circle(canvas, (int(u[0]), int(u[1])), 4, color, -1)
            cv2.circle(canvas, (int(g[0]), int(g[1])), 4, (255, 0, 0), -1)

        if major_flaws:
            print(f"Frame {i}: ⚠ High deviation on joints → {major_flaws}")

        cv2.imshow("Overlay", canvas)
        if cv2.waitKey(100) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

import cv2
import numpy as np

def render_overlay_video(seq_user, seq_golden, diff_map, w=640, h=480, threshold=0.2):
    for i in range(len(seq_user)):
        canvas = np.ones((h, w, 3), dtype=np.uint8) * 255
        user_frame = seq_user[i]
        golden_frame = seq_golden[i]
        
        # Ensure diff_map is an iterable with correct shape
        errors = diff_map[i] if isinstance(diff_map[i], np.ndarray) else np.array([diff_map[i]])

        # user_pts and golden_pts should be arrays of points
        user_pts = np.array(user_frame) * 300 + np.array([w // 2 - 150, h // 2])
        golden_pts = np.array(golden_frame) * 300 + np.array([w // 2 + 150, h // 2])

        major_flaws = []

        # Check if the points are 2D tuples
        if user_pts.ndim == 1:  # scalar, convert it to 2D array
            user_pts = np.array([user_pts])
        if golden_pts.ndim == 1:  # scalar, convert it to 2D array
            golden_pts = np.array([golden_pts])

        # Iterate through points and errors
        for j, (u, g, e) in enumerate(zip(user_pts, golden_pts, errors)):
            if e > threshold:
                color = (0, 0, 255)  # Red = flaw
                major_flaws.append((j, round(e, 3)))
            else:
                color = (0, 255, 0)  # Green = okay

            # Ensure u and g are tuples of integers and correctly plot them
            cv2.circle(canvas, (int(u[0]), int(u[1])), 4, color, -1)
            cv2.circle(canvas, (int(g[0]), int(g[1])), 4, (255, 0, 0), -1)

        if major_flaws:
            print(f"Frame {i}: ⚠ High deviation on joints → {major_flaws}")

        cv2.imshow("Overlay", canvas)
        if cv2.waitKey(100) & 0xFF == 27:
            break

    cv2.destroyAllWindows()

