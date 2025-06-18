import json
import time
import os

# Configs
FRAME_DELAY = 1.0  # seconds per simulated frame
INPUT_VIDEO_FLAGS = os.path.expanduser("~/formforge/sample_detection_output.json")
INPUT_WEARABLE = os.path.expanduser("~/formforge/sample_wearable_data.json")
OUTPUT_STREAM = os.path.expanduser("~/formforge/streamed_fatigue_feed.json")

def load_json(path):
    with open(path, "r") as f:
        return json.load(f)

def main():
    print("[✓] Starting simulated live fatigue stream...")
    video_data = load_json(INPUT_VIDEO_FLAGS)
    wearable_data = load_json(INPUT_WEARABLE)

    wearable_lookup = {
        entry["athlete_id"]: {r["timestamp"]: r for r in entry["readings"]}
        for entry in wearable_data
    }

    live_log = []

    for frame in video_data.get("frames", []):
        ts = frame["timestamp"]
        print(f"\n--- Time: {ts:.2f}s ---")

        for person in frame["people"]:
            aid = person["id"]
            fatigue = person.get("fatigue_flags", [])
            flaws = person.get("flaw_flags", [])
            wearables = wearable_lookup.get(aid, {}).get(ts, {})

            event = {
                "athlete_id": aid,
                "timestamp": ts,
                "fatigue": fatigue,
                "flaws": flaws,
                "wearables": wearables
            }

            print(json.dumps(event, indent=2))
            live_log.append(event)

        time.sleep(FRAME_DELAY)

    with open(OUTPUT_STREAM, "w") as f:
        json.dump(live_log, f, indent=2)

    print(f"\n[✓] Stream ended. Events saved to {OUTPUT_STREAM}")

if __name__ == "__main__":
    main()
