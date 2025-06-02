import os
import json
from datetime import datetime
from fpdf import FPDF
from formforge_tools.sport_detector import detect_sport_and_motion
from formforge_tools.pose_visualizer import get_pose_analysis_with_screenshots
from formforge_tools.joint_data_analyzer import analyze_joint_data
from formforge_tools.landmark_processor import process_landmarks
from formforge_tools.injury_predictor import predict_injury_risk
from formforge_tools.feedback_generator import generate_feedback

class UniversalReportGenerator(FPDF):
    def header(self):
        self.set_font("Helvetica", 'B', 16)
        self.cell(0, 10, "FormForge Full Session Analysis", ln=1, align="C")
        self.set_font("Helvetica", '', 12)
        self.cell(0, 10, f"Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=1)

    def chapter_title(self, title):
        self.set_font("Helvetica", 'B', 14)
        self.cell(0, 10, title, ln=1)
        self.set_font("Helvetica", '', 12)

    def chapter_body(self, text):
        self.multi_cell(0, 10, text)
        self.ln()

def generate_report(session_path):
    # Load data
    with open(os.path.join(session_path, "pose_analysis_output.json"), 'r') as f:
        pose_data = json.load(f)
    with open(os.path.join(session_path, "joint_data.csv"), 'r') as f:
        joint_csv_path = f.name
    with open(os.path.join(session_path, "output_landmarks.json"), 'r') as f:
        landmark_data = json.load(f)

    # Detect sport and motion
    sport, motion = detect_sport_and_motion(pose_data)

    # Generate analysis outputs
    pose_analysis_text, pose_images = get_pose_analysis_with_screenshots(pose_data, sport, motion, session_path)
    joint_summary, joint_charts = analyze_joint_data(joint_csv_path, sport, motion, session_path)
    landmark_summary = process_landmarks(landmark_data, sport, motion)
    injury_risk_text = predict_injury_risk(pose_data, sport, motion)
    feedback_text = generate_feedback(sport, injury_risk_text, joint_summary)

    # Create PDF
    pdf = UniversalReportGenerator()
    pdf.add_page()

    # Session Summary
    pdf.chapter_title(f"Session Summary - Sport: {sport} | Motion: {motion}")
    pdf.chapter_body(f"Session Path: {session_path}")

    # Pose Analysis with screenshots
    pdf.chapter_title("Pose Analysis")
    pdf.chapter_body(pose_analysis_text)
    for img_path in pose_images:
        pdf.image(img_path, w=150)
        pdf.ln()

    # Joint Data Analysis with charts
    pdf.chapter_title("Joint Data Analysis")
    pdf.chapter_body(joint_summary)
    for chart_path in joint_charts:
        pdf.image(chart_path, w=150)
        pdf.ln()

    # Landmark Output Summary
    pdf.chapter_title("Landmark Analysis")
    pdf.chapter_body(landmark_summary)

    # Injury Prevention
    pdf.chapter_title("Injury Prevention")
    pdf.chapter_body(injury_risk_text)

    # Improvement Feedback
    pdf.chapter_title("Improvement Suggestions")
    pdf.chapter_body(feedback_text)

    output_pdf_path = os.path.join(session_path, "session_report.pdf")
    pdf.output(output_pdf_path)
    print(f"✅ Report generated: {output_pdf_path}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python3 universal_report_generator.py <session_output_folder>")
        sys.exit(1)
    session_folder = sys.argv[1]
    generate_report(session_folder)
