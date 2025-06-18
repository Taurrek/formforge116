import glob, json
from datetime import datetime

def load_video_metrics(athlete_id: str, start: datetime, end: datetime):
    path_pattern = f"data/user/{athlete_id}/*.json"
    points = []
    for fname in glob.glob(path_pattern):
        with open(fname) as f:
            arr = json.load(f)
        for pt in arr:
            ts = datetime.fromisoformat(pt["timestamp"]).timestamp()
            if start.timestamp() <= ts <= end.timestamp():
                points.append({
                    "timestamp": ts,
                    "joint_velocity": float(pt["joint_velocity"])
                })
    points.sort(key=lambda p: p["timestamp"])
    return points
