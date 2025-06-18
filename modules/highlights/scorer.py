import numpy as np

def score_frames(frames, key='velocity'):
    """
    frames: list of dicts, each with a 'metrics' sub-dict holding movement magnitudes.
    Returns a list of (frame_index, score) sorted descending by score.
    """
    scored = []
    for i, f in enumerate(frames):
        score = f.get('metrics', {}).get(key, 0)
        scored.append((i, score))
    return sorted(scored, key=lambda x: x[1], reverse=True)

def top_n(frames, n=5, key='velocity'):
    """
    Returns the top-n frame indices by the given metric key.
    """
    scored = score_frames(frames, key)
    return [idx for idx, _ in scored[:n]]
