#!/usr/bin/env python3
import pandas as pd
import matplotlib.pyplot as plt
import os

CSV_PATH = os.path.join("reports", "risk_validation.csv")
OUT_DIR  = os.path.join("reports", "figures")
os.makedirs(OUT_DIR, exist_ok=True)

def main():
    df = pd.read_csv(CSV_PATH)
    plt.figure()
    plt.scatter(df["angle"], df["risk_score"])
    plt.xlabel("Joint Angle (°)")
    plt.ylabel("Risk Score")
    plt.title("Risk Score vs. Joint Angle")
    plt.tight_layout()
    out_path = os.path.join(OUT_DIR, "risk_vs_angle.png")
    plt.savefig(out_path)
    print(f"Figure saved to {out_path}")

if __name__ == "__main__":
    main()
