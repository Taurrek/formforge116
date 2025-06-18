import numpy as np
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

def normalize_pose_sequence(pose_sequence):
    centered = pose_sequence - np.mean(pose_sequence, axis=1, keepdims=True)
    scaled = centered / (np.std(centered, axis=1, keepdims=True) + 1e-8)
    return scaled

def align_sequences_dtw(seq1, seq2):
    # Flatten each frame: (25, 2) → (50,)
    series1 = [frame.flatten() for frame in seq1]
    series2 = [frame.flatten() for frame in seq2]
    _, path = fastdtw(series1, series2, dist=euclidean)

    aligned1, aligned2 = zip(*[(seq1[i], seq2[j]) for i, j in path])
    return np.array(aligned1), np.array(aligned2)

def compute_style_difference(golden_seq, user_seq):
    return np.linalg.norm(golden_seq - user_seq, axis=2)

def compute_difference_map(seq1, seq2):
    # Assumes both sequences are (frames, joints, 2)
    if seq1.shape != seq2.shape:
        raise ValueError("Sequences must be the same shape")
    return np.linalg.norm(seq1 - seq2, axis=-1)  # (frames, joints)
