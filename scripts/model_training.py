import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.ensemble import IsolationForest
import joblib

# Load data
data = pd.read_json('../data/sample_logs/users.json')

# Feature extraction and preprocessing
activity_data = pd.DataFrame(data['activityLogs'].explode().tolist())
activity_data['timestamp'] = pd.to_datetime(activity_data['timestamp'])
activity_data['timestamp'] = activity_data['timestamp'].astype(int) / 10**9

scaler = StandardScaler()
scaled_data = scaler.fit_transform(activity_data)

pca = PCA(n_components=2)
principal_components = pca.fit_transform(scaled_data)

# Anomaly detection
model = IsolationForest()
model.fit(principal_components)

# Save the model
joblib.dump(model, '../backend/models/anomaly_detector.joblib')