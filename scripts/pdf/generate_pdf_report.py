#!/usr/bin/env python3
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import pandas as pd
import os

CSV = "reports/risk_validation.csv"
FIG = "reports/figures/risk_vs_angle.png"
OUT = "reports/biomech_report.pdf"

def main():
    df = pd.read_csv(CSV)
    c = canvas.Canvas(OUT, pagesize=letter)
    width, height = letter

    # Title (updated for Phase 5 branding)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, height - 50, "FormForge Phase 5 Biomech Report")

    # Table header
    c.setFont("Helvetica-Bold", 12)
    y = height - 100
    c.drawString(50, y, "Subject")
    c.drawString(120, y, "Joint")
    c.drawString(200, y, "Angle")
    c.drawString(260, y, "Risk")
    c.setFont("Helvetica", 12)
    y -= 20

    # Table rows
    for _, row in df.iterrows():
        c.drawString(50, y, str(row.subject_id))
        c.drawString(120, y, row.joint)
        c.drawString(200, y, f"{row.angle:.1f}")
        c.drawString(260, y, f"{row.risk_score:.2f}")
        y -= 15
        if y < 100:
            c.showPage()
            y = height - 50

    # Add figure
    c.showPage()
    c.drawImage(FIG, 50, 200, width=500, preserveAspectRatio=True)

    c.save()
    print(f"PDF report generated → {OUT}")

if __name__ == "__main__":
    main()
