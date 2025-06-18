import os
import json
import numpy as np

GOLDEN_DB = "data/golden_registry.json"

def register_golden_model(name, path, metadata=None):
    metadata = metadata or {}
    model_entry = {
        "name": name,
        "path": path,
        "metadata": metadata
    }

    os.makedirs(os.path.dirname(GOLDEN_DB), exist_ok=True)
    if os.path.exists(GOLDEN_DB):
        with open(GOLDEN_DB, "r") as f:
            db = json.load(f)
    else:
        db = []

    db.append(model_entry)

    with open(GOLDEN_DB, "w") as f:
        json.dump(db, f, indent=2)
    print(f"✅ Registered golden model: {name}")

def list_golden_models():
    if not os.path.exists(GOLDEN_DB):
        return []
    with open(GOLDEN_DB, "r") as f:
        return json.load(f)

def load_golden_sequence(name):
    entries = list_golden_models()
    for e in entries:
        if e["name"] == name:
            return np.load(e["path"])
    raise ValueError(f"Golden model '{name}' not found.")
