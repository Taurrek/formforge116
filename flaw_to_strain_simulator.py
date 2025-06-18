#!/usr/bin/env python3
"""
flaw_to_strain_simulator.py

A simple engine that:
- Accepts a stream of flaw events (joint name + timestamp)
- Accumulates strain per joint over time, with decay
- Computes a fatigue metric per joint (e.g. running average of strain)
- Writes out:
    1) output/sim_output.json: the full timestamped strain timeline
    2) public/avatar_state.json: the current joint positions, strain, and fatigue
"""

import os
import json
import time
from typing import List, Dict, Any

# === CONFIG ===
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
AVATAR_JSON_PATH = os.path.join(os.path.dirname(__file__), "frontend", "public", "avatar_state.json")
SIM_OUTPUT_PATH = os.path.join(OUTPUT_DIR, "sim_output.json")

# Ensure directories exist
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.dirname(AVATAR_JSON_PATH), exist_ok=True)

# Simulation parameters
STRAIN_INCREASE_PER_FLAW = 5.0      # How much strain a flaw event adds
STRAIN_DECAY_RATE = 0.5             # Strain decays by this amount per time step
FATIGUE_SCALE = 0.1                 # Scales strain → fatigue

TIME_STEP = 0.1                     # seconds per simulation step
TOTAL_DURATION = 3.0                # simulate for 3 seconds

# Dummy flaw events: list of (timestamp, joint_name)
DUMMY_FLAWS: List[Dict[str, Any]] = [
    {"timestamp": 0.0, "joint": "elbow"},
    {"timestamp": 0.1, "joint": "shoulder"},
    {"timestamp": 0.2, "joint": "elbow"},
    {"timestamp": 0.3, "joint": "knee"},
    {"timestamp": 0.5, "joint": "elbow"},
    {"timestamp": 1.0, "joint": "shoulder"},
    {"timestamp": 1.5, "joint": "knee"},
    {"timestamp": 2.0, "joint": "elbow"},
    {"timestamp": 2.5, "joint": "shoulder"},
]

class FlawToStrainSimulator:
    def __init__(self):
        self.current_time = 0.0
        self.joint_strain: Dict[str, float] = {}
        self.joint_fatigue: Dict[str, float] = {}
        self.strain_timeline: List[Dict[str, Any]] = []

    def step(self, time_step: float, incoming_flaws: List[Dict[str, Any]]):
        """
        Advance simulation by time_step seconds, applying:
        - Any flaws whose timestamp <= current_time
        - Strain decay
        - Fatigue computation
        """
        # 1) Apply flaws at this timestamp
        for flaw in incoming_flaws:
            if abs(flaw["timestamp"] - self.current_time) < 1e-6:
                joint = flaw["joint"]
                self.joint_strain[joint] = self.joint_strain.get(joint, 0.0) + STRAIN_INCREASE_PER_FLAW

        # 2) Decay strain for each joint
        for joint, strain in list(self.joint_strain.items()):
            new_strain = max(0.0, strain - STRAIN_DECAY_RATE * time_step)
            self.joint_strain[joint] = new_strain

        # 3) Compute fatigue as a simple scaled running average of strain
        for joint, strain in self.joint_strain.items():
            prev_fatigue = self.joint_fatigue.get(joint, 0.0)
            new_fatigue = prev_fatigue + (strain * FATIGUE_SCALE * time_step)
            self.joint_fatigue[joint] = round(new_fatigue, 3)

        # 4) Record this timestamp’s strained joints
        strained_joints = {j: s for j, s in self.joint_strain.items() if s > 0}
        self.strain_timeline.append({
            "timestamp": round(self.current_time, 3),
            "strained_joints": strained_joints if strained_joints else {}
        })

        # 5) Write to avatar_state.json
        avatar_joints = []
        for joint, strain in self.joint_strain.items():
            fatigue = self.joint_fatigue.get(joint, 0.0)
            # Dummy x/y/z positions; replace with real data if available
            position = {
                "elbow": (120, 80),
                "shoulder": (200, 150),
                "knee": (300, 220)
            }.get(joint, (0, 0))
            avatar_joints.append({
                "name": joint,
                "x": position[0],
                "y": position[1],
                "z": 0.0,
                "strain": round(strain, 3),
                "fatigue": fatigue
            })

        avatar_state = {"timestamp": round(self.current_time, 3), "joints": avatar_joints}
        with open(AVATAR_JSON_PATH, "w") as f:
            json.dump(avatar_state, f, indent=2)

        # Advance time
        self.current_time += time_step

    def run(self):
        """
        Run simulation from t=0 to TOTAL_DURATION in steps of TIME_STEP.
        """
        flaw_index = 0
        total_flaws = len(DUMMY_FLAWS)

        while self.current_time <= TOTAL_DURATION + 1e-6:
            # Collect flaws whose timestamp == current_time
            step_flaws = []
            while flaw_index < total_flaws and abs(DUMMY_FLAWS[flaw_index]["timestamp"] - self.current_time) < 1e-6:
                step_flaws.append(DUMMY_FLAWS[flaw_index])
                flaw_index += 1

            self.step(TIME_STEP, step_flaws)
            time.sleep(0.05)  # slow down so you can watch AvatarStream in real time (optional)

        # After loop, write full strain timeline
        sim_output = {"strain_timeline": self.strain_timeline}
        with open(SIM_OUTPUT_PATH, "w") as f:
            json.dump(sim_output, f, indent=2)

        print(f"Simulation finished. Check {SIM_OUTPUT_PATH} and {AVATAR_JSON_PATH}.")


if __name__ == "__main__":
    sim = FlawToStrainSimulator()
    sim.run()
