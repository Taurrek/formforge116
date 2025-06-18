import numpy as np

class BiomechModel:
    def __init__(self):
        self.limb_params = {}

    def calibrate(self, joint_angles: dict, subject_info: dict):
        """
        joint_angles: {'hip': float, 'knee': float, 'ankle': float, …} [degrees of max flexion]
        subject_info: {'height': float, 'weight': float} in meters/kg
        
        Computes:
          - limb_lengths: based on height & Dempster’s segment ratios
          - joint_ranges: convert max flexion to radians
        """
        h = subject_info.get("height")
        if h is None or h <= 0:
            raise ValueError("subject_info.height must be > 0 (in meters)")

        # Dempster ratios for segment lengths (percent of height)
        ratios = {
            "thigh": 0.245,  # hip-to-knee
            "shank": 0.246   # knee-to-ankle
        }
        limb_lengths = {seg: ratios[seg] * h for seg in ratios}

        joint_ranges = {joint: np.deg2rad(angle) for joint, angle in joint_angles.items()}

        self.limb_params = {
            "lengths": limb_lengths,
            "ranges": joint_ranges,
            "subject": subject_info
        }
        return self.limb_params

    def predict_risk(self, joint_df):
        """
        joint_df: list of dicts [{ 'joint': str, 'angle': float, … }, …]
        Returns: {'risk_score': float}
        """
        # TODO: replace with real torque/risk formula
        risk = np.random.rand()
        return {"risk_score": float(risk)}
