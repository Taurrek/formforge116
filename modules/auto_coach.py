import json

def generate_coaching_feedback(comparison_json):
    score_diff = comparison_json.get("score_diff", 0)
    notes = comparison_json.get("notes", "")

    feedback = []

    if score_diff > 10:
        feedback.append("Significant gap detected between athlete and golden model.")
    elif score_diff > 5:
        feedback.append("Moderate gap detected. Athlete has room for improvement.")
    else:
        feedback.append("Athlete performance is close to golden standard.")

    if "knee drive" in notes.lower():
        feedback.append("Focus on knee drive mechanics using resistance band drills.")
    if "core" in notes.lower() or "stability" in notes.lower():
        feedback.append("Recommend core stability work: planks, deadbugs, and anti-rotation exercises.")
    if "hip" in notes.lower():
        feedback.append("Emphasize hip mobility and glute activation drills.")

    return {
        "feedback": " ".join(feedback),
        "score_diff": score_diff,
        "notes": notes
    }
