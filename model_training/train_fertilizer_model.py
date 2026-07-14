import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv("dataset/fertilizer.csv")

encoder_soil = LabelEncoder()
encoder_crop = LabelEncoder()
encoder_fertilizer = LabelEncoder()

df['SoilType'] = encoder_soil.fit_transform(df['SoilType'])
df['CropType'] = encoder_crop.fit_transform(df['CropType'])
df['Fertilizer'] = encoder_fertilizer.fit_transform(df['Fertilizer'])

X = df.drop('Fertilizer', axis=1)
y = df['Fertilizer']

model = RandomForestClassifier(random_state=42)

model.fit(X, y)

joblib.dump(model, "models/fertilizer_model.pkl")
joblib.dump(encoder_soil, "models/soil_encoder.pkl")
joblib.dump(encoder_crop, "models/crop_encoder.pkl")
joblib.dump(encoder_fertilizer, "models/fertilizer_encoder.pkl")

print("Fertilizer Model Trained Successfully")