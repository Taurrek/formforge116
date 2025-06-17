#!/usr/bin/env python3
"""
golden_athlete_registry.py

Scaffold for logging and managing “golden athlete” motion profiles.
Each golden model is saved as a JSON file under public/golden_models/.
"""

import os
import json
import logging
from typing import Dict, Any, List


# === CONFIGURATION ===
GOLDEN_MODELS_DIR = os.path.join(
    os.path.dirname(__file__), "public", "golden_models"
)
os.makedirs(GOLDEN_MODELS_DIR, exist_ok=True)

# Set up basic logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)
logger = logging.getLogger(__name__)


class GoldenAthleteRegistry:
    """
    Manages golden athlete reference models.
    """

    def __init__(self, storage_dir: str = GOLDEN_MODELS_DIR):
        self.storage_dir = storage_dir
        logger.info(f"GoldenAthleteRegistry initialized with storage: {self.storage_dir}")

    def _model_path(self, sport: str, position: str, joint_cluster: str) -> str:
        """
        Compute the JSON filename for a given sport/position/joint cluster.
        e.g., "basketball_pointguard_upper_body.json"
        """
        filename = f"{sport.lower()}_{position.lower()}_{joint_cluster.lower()}.json"
        return os.path.join(self.storage_dir, filename)

    def add_golden_model(self, sport: str, position: str, joint_cluster: str, data: Dict[str, Any]) -> None:
        """
        Save a new golden model to disk.
        - sport: e.g., "Basketball"
        - position: e.g., "PointGuard"
        - joint_cluster: e.g., "UpperBody"
        - data: dictionary containing the reference motion data (joint angles, timestamps, etc.)
        """
        path = self._model_path(sport, position, joint_cluster)
        try:
            with open(path, "w") as f:
                json.dump(data, f, indent=2)
            logger.info(f"Saved golden model: {path}")
        except Exception as e:
            logger.error(f"Failed to write golden model to {path}: {e}")
            raise

    def load_golden_model(self, sport: str, position: str, joint_cluster: str) -> Dict[str, Any]:
        """
        Load a golden model from disk. Returns the parsed JSON dict.
        Raises FileNotFoundError if the model does not exist.
        """
        path = self._model_path(sport, position, joint_cluster)
        if not os.path.exists(path):
            msg = f"Golden model not found at {path}"
            logger.error(msg)
            raise FileNotFoundError(msg)

        with open(path, "r") as f:
            data = json.load(f)
        logger.info(f"Loaded golden model: {path}")
        return data

    def list_all_models(self) -> List[str]:
        """
        Return a list of all saved golden-model filenames (without full path).
        """
        files = [
            fname
            for fname in os.listdir(self.storage_dir)
            if fname.endswith(".json")
        ]
        logger.info(f"Found {len(files)} golden model(s).")
        return files

    def compare_to_gold_standard(
        self,
        current_frame_data: Dict[str, Any],
        sport: str,
        position: str,
        joint_cluster: str
    ) -> Dict[str, Any]:
        """
        Compare a current frame’s joint data against the saved golden model.
        Returns a structure like { 'joint_name': deviation_value, ... }.

        current_frame_data should include the same keys as the golden model (e.g., joint angles).
        """
        try:
            golden = self.load_golden_model(sport, position, joint_cluster)
        except FileNotFoundError as e:
            logger.error("Comparison failed: golden model missing.")
            raise

        # === STUB: implement your actual comparison logic here ===
        # Example idea: for each joint, compute absolute difference in angle
        deviations = {}
        for joint, curr_val in current_frame_data.items():
            gold_val = golden.get(joint)
            if gold_val is None:
                logger.warning(f"Joint '{joint}' not found in golden model; skipping.")
                continue
            # Simple deviation—replace with your own metric
            deviations[joint] = abs(curr_val - gold_val)

        # Compute an overall score or percentage if desired
        deviations["_summary"] = {
            "max_deviation": max(deviations.values()) if deviations else 0,
            "average_deviation": (sum(deviations.values()) / len(deviations)) if deviations else 0
        }

        logger.info(f"Computed deviations for {sport}/{position}/{joint_cluster}")
        return deviations

    def export_all_models_to_public(self) -> None:
        """
        (Optional) If you have multiple in-memory models, write them all to disk.
        For now, this is identical to ensuring the directory exists.
        """
        os.makedirs(self.storage_dir, exist_ok=True)
        logger.info("Ensured public golden_models directory exists.")


# === USAGE EXAMPLE (run as script) ===
if __name__ == "__main__":
    registry = GoldenAthleteRegistry()

    # Example: Add a dummy golden model
    dummy_data = {
        "joint_1": 30.0,
        "joint_2": 45.5,
        "joint_3": 12.1
        # ... etc. (timestamps, frame indices, etc.)
    }
    registry.add_golden_model(
        sport="Basketball",
        position="PointGuard",
        joint_cluster="UpperBody",
        data=dummy_data
    )

    # Example: Load and compare
    try:
        current = {"joint_1": 28.4, "joint_2": 47.0, "joint_3": 10.0}
        diffs = registry.compare_to_gold_standard(
            current_frame_data=current,
            sport="Basketball",
            position="PointGuard",
            joint_cluster="UpperBody"
        )
        print("Deviations:", diffs)
    except FileNotFoundError:
        print("Golden model not yet created.")

    # List all saved models
    print("All models:", registry.list_all_models())
