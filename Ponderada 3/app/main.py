# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model
import os

# Create the app
app = FastAPI()

# Load trained Pipeline
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model/heart_predict")

model = load_model(MODEL_PATH)

# Create input/output pydantic models
input_model = create_model("heart_predict_input", **{'age': 0.49343279004096985, 'sex': 1.0, 'cp': 0.0, 'trestbps': 2.1601908206939697, 'chol': 0.7830833196640015, 'fbs': 0.0, 'restecg': 2.0, 'thalach': 0.41045764088630676, 'exang': 0.0, 'oldpeak': -0.7349136471748352, 'slope': 1.0, 'ca': 0.0, 'thal': 2.0})
output_model = create_model("heart_predict_output", prediction=0)


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
