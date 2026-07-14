import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("dataset/Crop_recommendation.csv")

# Features
X = df[['N','P','K','temperature','humidity','ph','rainfall']]

# Target
y = df['label']

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Save model
joblib.dump(model, "models/crop_model.pkl")

print("Crop Model Trained Successfully")