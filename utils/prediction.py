import joblib
import numpy as np

# Load Models
crop_model = joblib.load("models/crop_model.pkl")
fertilizer_model = joblib.load("models/fertilizer_model.pkl")
yield_model = joblib.load("models/yield_model.pkl")

# Load Encoders
soil_encoder = joblib.load("models/soil_encoder.pkl")
crop_encoder = joblib.load("models/crop_encoder.pkl")
fertilizer_encoder = joblib.load("models/fertilizer_encoder.pkl")


# ---------------- Crop Prediction ---------------- #

def predict_crop(N, P, K, temperature, humidity, ph, rainfall):

    data = np.array([[N, P, K,
                      temperature,
                      humidity,
                      ph,
                      rainfall]])

    prediction = crop_model.predict(data)

    return prediction[0]


# ---------------- Fertilizer Prediction ---------------- #

def predict_fertilizer(temp,
                       humidity,
                       moisture,
                       soil,
                       crop,
                       nitrogen,
                       potassium,
                       phosphorus):

    soil = soil_encoder.transform([soil])[0]

    crop = crop_encoder.transform([crop])[0]

    data = np.array([[temp,
                      humidity,
                      moisture,
                      soil,
                      crop,
                      nitrogen,
                      potassium,
                      phosphorus]])

    prediction = fertilizer_model.predict(data)

    fertilizer = fertilizer_encoder.inverse_transform(prediction)

    return fertilizer[0]


# ---------------- Yield Prediction ---------------- #

def predict_yield(rainfall,
                  temperature,
                  soil_quality,
                  fertilizer):

    data = np.array([[rainfall,
                      temperature,
                      soil_quality,
                      fertilizer]])

    prediction = yield_model.predict(data)

    return round(prediction[0],2)