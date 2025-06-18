import json
import os

def export_flaw_report(diff_map, threshold=0.2, out_path="output/real_time_flaw_report.json"):
    """
    Export the flaw report as a JSON file.
    This function processes the diff_map and exports any detected flaws above the threshold.
    """

    # Initialize the report list
    report = []

    # Iterate through each frame's errors in the diff_map
    for i, frame_errors in enumerate(diff_map):
        # Ensure frame_errors is iterable, even if it's a single value
        if not isinstance(frame_errors, (list, tuple)):
            frame_errors = [frame_errors]  # Convert single value to list

        # Collect the flaws for this frame, filtering by threshold
        flaws = [{"joint": int(j), "error": float(round(e, 4))} for j, e in enumerate(frame_errors) if e > threshold]
        
        # Add the frame's flaws to the report if any are found
        if flaws:
            report.append({"frame": i, "flaws": flaws})

    # Create the output directory if it doesn't exist
    os.makedirs(os.path.dirname(out_path), exist_ok=True)

    # Write the report to the specified JSON file
    with open(out_path, "w") as f:
        json.dump(report, f, indent=4)

