import sys
import json
import os

def compare_motion_ranges(session_path, baseline_path, tolerance=10.0):
    motion_range_path = os.path.join(session_path, "motion_ranges.json")
    if not os.path.exists(motion_range_path):
        print(f"❌ Motion ranges not found at {motion_range_path}")
        return

    with open(motion_range_path, "r") as f:
        session_ranges = json.load(f)

    with open(baseline_path, "r") as f:
        baseline_ranges = json.load(f)

    flaws = {}

    for joint, session_range in session_ranges.items():
        if joint not in baseline_ranges:
            continue
        base_range = baseline_ranges[joint]
        session_min, session_max = session_range
        base_min, base_max = base_range

        if abs(session_min - base_min) > tolerance or abs(session_max - base_max) > tolerance:
            flaws[joint] = {
                "session": session_range,
                "baseline": base_range,
                "difference": [
                    round(session_min - base_min, 2),
                    round(session_max - base_max, 2)
                ]
            }

    output_path = os.path.join(session_path, "flaws.json")
    with open(output_path, "w") as f:
        json.dump(flaws, f, indent=2)

    print(f"🔍 Flaw analysis complete. Results saved to {output_path}")
    if flaws:
        print(f"⚠️  Detected flaws in {len(flaws)} joint(s).")
    else:
        print("✅ No significant flaws detected!")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python scripts/compare_to_baseline.py <session_path> <baseline_path>")
    else:
        session = sys.argv[1]
        baseline = sys.argv[2]
        compare_motion_ranges(session, baseline)

