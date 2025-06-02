import sys
import json
import os

def create_baseline(session_path, output_name="golden_baseline"):
    motion_range_path = os.path.join(session_path, "motion_ranges.json")
    if not os.path.exists(motion_range_path):
        print(f"❌ Motion ranges not found at {motion_range_path}")
        return

    with open(motion_range_path, "r") as f:
        motion_ranges = json.load(f)

    output_dir = "baselines"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{output_name}.json")

    with open(output_path, "w") as f:
        json.dump(motion_ranges, f, indent=2)

    print(f"✅ Baseline saved to {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python scripts/create_baseline.py <session_path> [baseline_name]")
    else:
        session = sys.argv[1]
        name = sys.argv[2] if len(sys.argv) > 2 else "golden_baseline"
        create_baseline(session, name)
