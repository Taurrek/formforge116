from golden_model_registry import add_or_update_model, list_models_in_registry, get_model_from_registry, update_model_status, get_models_by_error_threshold, delete_model, bulk_add_or_update_models, bulk_delete_models

# Test adding or updating a model with metadata
metadata = {'dataset': 'CIFAR-10', 'epochs': 50, 'learning_rate': 0.001}
add_or_update_model('model_001', 0.02, 'valid', metadata)
add_or_update_model('model_002', 0.05, 'invalid')

# List all models
print("All Models:", list_models_in_registry())

# Retrieve a specific model
print("Model 001:", get_model_from_registry('model_001'))

# Update model status
update_model_status('model_001', 'under review')

# Get models by error threshold (<= 0.05)
print("Models with error <= 0.05:", get_models_by_error_threshold(0.05))

# Delete a model
delete_model('model_002')

# List models after deletion
print("Models after deletion:", list_models_in_registry())

# Bulk add/update models
bulk_add_or_update_models({
    'model_003': (0.01, 'valid', {'dataset': 'ImageNet', 'epochs': 100}),
    'model_004': (0.04, 'valid', {'dataset': 'MNIST', 'epochs': 50})
})

# Bulk delete models
bulk_delete_models(['model_003', 'model_004'])
