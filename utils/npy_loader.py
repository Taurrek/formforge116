import numpy as np
import os

def load_npy_sequence(directory):
    files = sorted([f for f in os.listdir(directory) if f.endswith('.npy')])
    if not files:
        raise ValueError(f"No .npy files found in {directory}")

    sequence = []
    for f in files:
        arr = np.load(os.path.join(directory, f))

        # Typical OpenPose shape: (frames, joints, 3)
        if arr.ndim == 3 and arr.shape[-1] == 3:
            sequence.append(arr[:, :, :2])  # Drop confidence if needed

        # Weird shape: (frames, 2, joints, 3) — transpose it
        elif arr.ndim == 4 and arr.shape[1] == 2:
            arr = np.transpose(arr, (0, 2, 1, 3))  # → (frames, joints, 2, 3)
            arr = arr[:, :, 0, :2]  # drop confidence + dim
            sequence.append(arr)

        # Shape like (frames, 2, 3)? Flip axis
        elif arr.ndim == 3 and arr.shape[1] == 2 and arr.shape[2] == 3:
            arr = np.transpose(arr, (0, 2, 1))  # → (frames, 3, 2)
            arr = arr[:, :2, :]  # drop confidence
            arr = np.transpose(arr, (0, 2, 1))  # → (frames, 2, 2)
            sequence.append(arr)

        else:
            print(f"⚠️ Unrecognized shape: {arr.shape} in file {f}")
            continue

    return np.concatenate(sequence, axis=0)
