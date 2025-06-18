import json
import os
from datetime import datetime
import logging

# Set up logging configuration
logging.basicConfig(filename='model_registry.log', level=logging.INFO, format='%(asctime)s - %(message)s')

REGISTRY_PATH = os.path.join(os.getcwd(), 'golden_model_registry.json')

# Helper function to load the existing registry (returns an empty dict if not found)
def load_registry():
    if os.path.exists(REGISTRY_PATH):
        with open(REGISTRY_PATH, 'r') as file:
            return json.load(file)
    return {}

# Helper function to save the registry to the JSON file
def save_registry(registry):
    with open(REGISTRY_PATH, 'w') as file:
        json.dump(registry, file, indent=4)

# Log action function
def log_action(action, model_id):
    logging.info(f"Action: {action}, Model ID: {model_id}")

# Validate model (based on error threshold)
def validate_model(error, threshold=0.05):
    if error > threshold:
        print(f"Model error ({error}) exceeds threshold ({threshold}). Model will not be added.")
        return False
    return True

# Add or update a model with versioning and metadata
def add_or_update_model(model_id, error, status='valid', metadata=None):
    if not validate_model(error):
        return

    registry = load_registry()

    # Check if model exists, and set the version to 1 if it's a new model, otherwise increment the version
    version = 1
    if model_id in registry:
        # Increment version if the model already exists
        version = registry[model_id].get('version', 0) + 1

    model_entry = {
        'error': error,
        'status': status,
        'timestamp': datetime.now().isoformat(),
        'version': version,
        'metadata': metadata or {}  # Store metadata like hyperparameters, datasets, etc.
    }

    registry[model_id] = model_entry
    save_registry(registry)
    log_action("Add/Update", model_id)

# Update the status of an existing model
def update_model_status(model_id, status):
    registry = load_registry()
    if model_id in registry:
        registry[model_id]['status'] = status
        registry[model_id]['timestamp'] = datetime.now().isoformat()  # Update timestamp
        save_registry(registry)
        log_action("Update Status", model_id)
    else:
        print(f"Error: Model {model_id} not found.")

# Get a model from the registry by ID
def get_model_from_registry(model_id):
    registry = load_registry()
    return registry.get(model_id)

# List all models in the registry
def list_models_in_registry():
    registry = load_registry()
    return list(registry.keys())

# Get models with error within a certain threshold
def get_models_by_error_threshold(threshold):
    registry = load_registry()
    return {model_id: data for model_id, data in registry.items() if data['error'] <= threshold}

# Delete a model from the registry (if needed)
def delete_model(model_id):
    registry = load_registry()
    if model_id in registry:
        del registry[model_id]
        save_registry(registry)
        log_action("Delete", model_id)
    else:
        print(f"Error: Model {model_id} not found.")

# Bulk add or update models
def bulk_add_or_update_models(models):
    for model_id, (error, status, metadata) in models.items():
        add_or_update_model(model_id, error, status, metadata)

# Bulk delete models
def bulk_delete_models(model_ids):
    registry = load_registry()
    for model_id in model_ids:
        if model_id in registry:
            del registry[model_id]
            log_action("Bulk Delete", model_id)
    save_registry(registry)
