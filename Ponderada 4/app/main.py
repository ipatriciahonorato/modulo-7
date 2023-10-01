# -*- coding: utf-8 -*-

import os
import boto3
import pandas as pd
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from pycaret.classification import load_model, predict_model
from pydantic import BaseModel

# Create the app
app = FastAPI()

# Configurar cliente S3
s3 = boto3.client('s3', region_name='us-east-1')
bucket_name = 'meu-bucket-inteli-patricia'
model_file_name = 'heart_predict.pkl'

# Baixe o modelo do S3 e carregue-o para o FastAPI
local_model_path = "local_heart_predict.pkl"
s3.download_file(bucket_name, model_file_name, local_model_path)
model = load_model(local_model_path)

# Authentication setup
SECRET = "perseu-e-fumaca"
manager = LoginManager(SECRET, tokenUrl='/auth/token', use_cookie=False)
fake_users_db = {"testuser": {"username": "testuser", "password": "testpassword", "disabled": False}}

def get_current_user(token: str = Depends(manager)):
    try:
        payload = manager.decode_token(token)
    except InvalidCredentialsException:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
    
    user = fake_users_db.get(payload.get("sub"))
    if user is None or user.get("disabled"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Unauthorized")
    
    return user

@app.post('/auth/token')
def login(data: dict):
    username = data.get('username')
    password = data.get('password')
    user = fake_users_db.get(username)

    if user is None or password != user.get("password"):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    
    return {'access_token': manager.create_access_token(data={'sub': username})}

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
def predict(data: HeartPredictInput, user=Depends(get_current_user)):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"prediction": predictions["prediction_label"].iloc[0]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)