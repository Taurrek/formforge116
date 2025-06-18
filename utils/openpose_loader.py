import json
import numpy as np

def load_openpose_sequence(json_paths, num_joints=17):
    sequence = []
    for path in json_paths:
        with open(path) as f:
            data = json.load(f)
            if not data['people']:
                continue
            keypoints = data['people'][0]['pose_keypoints_2d'][:num_joints * 3]
            xy = np.array(keypoints).reshape((num_joints, 3))[:, :2]
            sequence.append(xy)
    return np.array(sequence)
