import json
from collections import defaultdict

def process_fatigue_events(detection_json_path, output_path="video_fatigue_flags_multi.json"):
    with open(detection_json_path, "r") as f:
        data = json.load(f)

    # Assume each frame has list of poses, each with unique "athlete_id"
    athlete_events = defaultdict(list)

    for frame in data.get("frames", []):
        timestamp = frame.get("timestamp")
        for person in frame.get("people", []):
            athlete_id = person.get("id", "unknown")
            fatigue_flags = person.get("fatigue_flags", [])
            flaw_flags = person.get("flaw_flags", [])

            for flag in fatigue_flags:
                athlete_events[athlete_id].append({
                    "timestamp": timestamp,
                    "type": "fatigue",
                    "value": flag
                })

            for flag in flaw_flags:
                athlete_events[athlete_id].append({
                    "timestamp": timestamp,
                    "type": "flaw",
                    "value": flag
                })

    # Structure as list for frontend ease
    structured_output = []
    for athlete_id, events in athlete_events.items():
        structured_output.append({
            "athlete_id": athlete_id,
            "events": sorted(events, key=lambda x: x["timestamp"])
        })

    with open(output_path, "w") as f:
        json.dump(structured_output, f, indent=2)

    print(f"[✓] Saved multi-athlete fatigue log to {output_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python multi_athlete_fatigue_logger.py <detection_json>")
    else:
        process_fatigue_events(sys.argv[1])
