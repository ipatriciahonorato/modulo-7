# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
from pydantic import BaseModel
import os

# Create the app
app = FastAPI()

# Load trained Pipeline
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model/heart_predict")

model = load_model(MODEL_PATH)

# Define Pydantic models
class HeartPredictInput(BaseModel):
    age: float
    sex: float
    cp: float
    trestbps: float
    chol: float
    fbs: float
    restecg: float
    thalach: float
    exang: float
    oldpeak: float
    slope: float
    ca: float
    thal: float

class HeartPredictOutput(BaseModel):
    prediction: int

# Define predict function
@app.post("/predict", response_model=HeartPredictOutput)
def predict(data: HeartPredictInput):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
