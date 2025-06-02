# formforge_tools/ai_note_assistant.py

def generate_ai_notes(session_summary, performance_metrics):
    """
    Generate AI coach notes and motivational feedback.

    Args:
        session_summary (str): Summary of session.
        performance_metrics (dict): Key performance indicators.

    Returns:
        str: AI-generated notes.
    """
    notes = f"Session Summary: {session_summary}\n"
    notes += "Performance Highlights:\n"
    for k, v in performance_metrics.items():
        notes += f"- {k}: {v}\n"
    notes += "Keep up the good work! Focus on consistency and recovery."

    return notes

if __name__ == "__main__":
    dummy_summary = "Good session with steady improvement."
    dummy_metrics = {"speed": 7.2, "flexibility": 6.5, "power": 8.0}
    print(generate_ai_notes(dummy_summary, dummy_metrics))
