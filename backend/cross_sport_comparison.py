from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import numpy as np

def compare_sport_models(features_1, labels_1, features_2, labels_2):
    # Split the data for model training
    X_train_1, X_test_1, y_train_1, y_test_1 = train_test_split(features_1, labels_1, test_size=0.2, random_state=42)
    X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(features_2, labels_2, test_size=0.2, random_state=42)
    
    # Train a RandomForest Classifier for the first sport model
    model_1 = RandomForestClassifier(n_estimators=100, random_state=42)
    model_1.fit(X_train_1, y_train_1)
    
    # Train a RandomForest Classifier for the second sport model
    model_2 = RandomForestClassifier(n_estimators=100, random_state=42)
    model_2.fit(X_train_2, y_train_2)
    
    # Predict using both models
    predictions_1 = model_1.predict(X_test_1)
    predictions_2 = model_2.predict(X_test_2)
    
    # Calculate accuracy for both models
    accuracy_1 = accuracy_score(y_test_1, predictions_1)
    accuracy_2 = accuracy_score(y_test_2, predictions_2)
    
    # Compare accuracy scores between the two models
    comparison_result = {
        "accuracy_model_1": accuracy_1,
        "accuracy_model_2": accuracy_2,
        "comparison_score": np.abs(accuracy_1 - accuracy_2)
    }
    
    return comparison_result

# Example usage:
features_1, labels_1 = load_and_preprocess_data("sport_1_data.csv")
features_2, labels_2 = load_and_preprocess_data("sport_2_data.csv")

comparison_result = compare_sport_models(features_1, labels_1, features_2, labels_2)
print(comparison_result)
