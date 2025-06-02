import os
import json
import numpy as np
import cv2

# === Day 21: MVP Finalizer ===

def summarize_session(session_name):
    session_path = os.path.join("sessions", session_name)
    score_file = os.path.join(session_path, "score.json")
    flags_file = os.path.join(session_path, "flags.json")
    overlay_file = os.path.join(session_path, "ghost_overlay.mp4")

    print(f"\n🔍 Summary for {session_name}")

    if os.path.exists(score_file):
        with open(score_file) as f:
            score = json.load(f)["motion_score"]
            print(f"  - Motion Score: {score:.2f}")
    else:
        print("  - ❌ No score.json found")

    if os.path.exists(flags_file):
        with open(flags_file) as f:
            flags = json.load(f)
            if flags["flaws"]:
                print(f"  - ❗ Flaws Detected: {len(flags['flaws'])}")
                for flaw in flags["flaws"]:
                    print(f"     • {flaw['joint']} → {flaw['deviation']} ({flaw['type']})")
            else:
                print("  - ✅ No flaws detected")
    else:
        print("  - ⚠️ No flags.json found")

    if os.path.exists(overlay_file):
        print(f"  - 🎥 Ghost overlay video exists.")
    else:
        print("  - ⚠️ No ghost overlay video found.")

def list_sessions():
    return sorted([
        name for name in os.listdir("sessions")
        if os.path.isdir(os.path.join("sessions", name))
    ])

if __name__ == "__main__":
    print("🏁 Running MVP Finalizer...\n")
    sessions = list_sessions()
    if not sessions:
        print("❌ No sessions found.")
    for session in sessions:
        summarize_session(session)
    print("\n✅ MVP summary complete. You're ready to deploy FormForge!")
