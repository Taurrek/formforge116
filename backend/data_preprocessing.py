import pandas as pd
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(file_path):
    # Load CSV data
    data = pd.read_csv(file_path)
    
    # Assuming the last column is the label
    features = data.iloc[:, :-1].values
    labels = data.iloc[:, -1].values

    # Normalize the features (this helps with cross-sport comparison)
    scaler = StandardScaler()
    normalized_features = scaler.fit_transform(features)

    return normalized_features, labels

# Example usage:
file_path = "athlete_data.csv"
features, labels = load_and_preprocess_data(file_path)
