# FormForge: Motion AI MVP (CPU-Only)

FormForge is a Python-based human motion analysis app using OpenPose keypoints to extract, normalize, score, detect flaws, generate feedback, and summarize sessions.

## ✅ MVP Pipeline (21 Scripts)

- Extract keypoints from video frames
- Normalize and compare motion
- Score user movement (0–100 scale)
- Detect flaws & suggest corrections
- Ghost overlay & final summary report

## 🧰 How to Run

```bash
# Run all scripts in order
for day in {1..15}; do
  python3 formforge_day01_to_21/formforge_day${day}_*.py
done

for day in {16..21}; do
  python3 formforge_day01_to_21/formforge_day${day}_*.py
done
```

## 📁 Folder Structure

- `formforge_day01_to_21/`: All pipeline scripts
- `sessions/`: Saved motion sessions (JSON, NPY, etc)
- `test_output/`: Keypoints, visualizations, etc

## 🔧 Requirements

```bash
pip install -r requirements.txt
```

Runs on any machine with Python 3. No GPU or CUDA required.

## 🔍 Known Issues

- Some test sessions are missing input video or score files
- Ghost overlays depend on presence of `input_video.mp4` in session folder
