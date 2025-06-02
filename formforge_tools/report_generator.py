# formforge_tools/report_generator.py

from fpdf import FPDF

def generate_pdf_report(session_analyses, output_file="report.pdf"):
    """
    Generate a PDF report combining multiple session analyses.

    Args:
        session_analyses (dict): Key-value pairs of analysis names and results.
        output_file (str): Output filename.

    Returns:
        None
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "FormForge Session Report", ln=True, align="C")

    for name, result in session_analyses.items():
        pdf.ln(10)
        pdf.cell(0, 10, f"{name}:", ln=True)
        pdf.multi_cell(0, 10, str(result))

    pdf.output(output_file)

if __name__ == "__main__":
    dummy_analyses = {
        "Pitch Analysis": {"flaw_scores": {"arm_angle": 0.1}},
        "Fatigue Detection": {"fatigue_level": 0.4}
    }
    generate_pdf_report(dummy_analyses)
    print("Report generated: report.pdf")
