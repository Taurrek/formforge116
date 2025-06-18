# Ensure proper diff_map structure and pass it to export_flaw_report

from formforge.modules.neural_style import dynamic_time_warping, compute_difference_map, export_flaw_report

def real_time_pipeline(user_data_stream, golden_data_stream):
    # Align user and golden data using dynamic time warping
    user_aligned, golden_aligned = dynamic_time_warping(user_data_stream, golden_data_stream)

    # Compute the difference map between the aligned data
    diff_map = compute_difference_map(user_aligned, golden_aligned)

    # Ensure diff_map is in the correct format (list of lists)
    # Assuming diff_map should be a 2D structure (list of lists)
    if isinstance(diff_map, int):
        diff_map = [[diff_map]]

    # Export the flaw report
    export_flaw_report(diff_map, threshold=0.2, out_path="output/real_time_flaw_report.json")

    return diff_map
