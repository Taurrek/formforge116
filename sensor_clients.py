import csv
from datetime import datetime

def fetch_whoop_data(athlete_id: str, since: datetime):
    """Read Whoop CSV and return all points ≥ `since`."""
    fname = f"data/whoop/{athlete_id}.csv"
    points = []
    with open(fname) as f:
        reader = csv.DictReader(f)
        for row in reader:
            ts = datetime.fromisoformat(row["timestamp"]).timestamp()
            if ts >= since.timestamp():
                points.append({
                    "timestamp": ts,
                    "heart_rate": float(row["heart_rate"])
                })
    points.sort(key=lambda p: p["timestamp"])
    return points
