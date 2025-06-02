# formforge_tools/multi_session_comparator.py

def compare_sessions(session_list):
    """
    Compare multiple sessions and highlight changes.

    Args:
        session_list (list): List of session dicts with metrics.

    Returns:
        dict: {
            "improvements": dict,
            "regressions": dict,
            "summary": str
        }
    """
    # Placeholder: simple difference between first and last session for each metric
    first = session_list[0]
    last = session_list[-1]
    improvements = {}
    regressions = {}
    for metric in first.keys():
        diff = last[metric] - first[metric]
        if diff > 0:
            improvements[metric] = diff
        elif diff < 0:
            regressions[metric] = diff

    summary = f"Compared {len(session_list)} sessions: {len(improvements)} improvements, {len(regressions)} regressions."
    return {
        "improvements": improvements,
        "regressions": regressions,
        "summary": summary
    }

if __name__ == "__main__":
    dummy_sessions = [
        {"speed": 5, "flexibility": 3, "power": 4},
        {"speed": 6, "flexibility": 2.5, "power": 5},
        {"speed": 7, "flexibility": 3.5, "power": 5.5},
    ]
    print(compare_sessions(dummy_sessions))
