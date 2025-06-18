#!/usr/bin/env python3
import os, glob, json, csv, requests

API_BASE = "http://127.0.0.1:8003/api/biomech"
CALIBRATE_URL = f"{API_BASE}/calibrate"
PREDICT_URL   = f"{API_BASE}/predict"
DATA_DIR      = "data/calibration"
REPORT_FILE   = "reports/risk_validation.csv"

def main():
    os.makedirs("reports", exist_ok=True)
    with open(REPORT_FILE, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["subject_id", "joint", "angle", "risk_score"])
        for path in sorted(glob.glob(os.path.join(DATA_DIR, "subject_*.json"))):
            data = json.load(open(path))
            sid = data["subject_id"]
            # calibrate
            requests.post(CALIBRATE_URL, json={
                "joint_angles": data["joint_angles"],
                "subject_info":  data["subject_info"]
            }).raise_for_status()
            # predict per joint
            for j, a in data["joint_angles"].items():
                resp = requests.post(PREDICT_URL, json={"joint_df":[{"joint":j,"angle":a}]})
                resp.raise_for_status()
                writer.writerow([sid, j, a, resp.json()["risk_score"]])
    print("Validation complete →", REPORT_FILE)

if __name__=="__main__":
    main()
