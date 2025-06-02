# backend/report_generator.py
from fpdf import FPDF

def generate_report(session_data, output_path="report.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="FormForge Motion Analysis Report", ln=True, align='C')
    pdf.ln(10)

    for key, val in session_data.items():
        pdf.cell(200, 10, txt=f"{key}: {val}", ln=True)

    pdf.output(output_path)
    return output_path
