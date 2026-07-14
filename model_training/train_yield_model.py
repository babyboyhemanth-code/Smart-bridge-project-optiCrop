import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("dataset/yield.csv")

X = df[['Rainfall',
        'Temperature',
        'SoilQuality',
        'Fertilizer']]

y = df['ExpectedYield']

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "models/yield_model.pkl")

print("Yield Model Trained Successfully")