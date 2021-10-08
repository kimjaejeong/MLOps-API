from fastapi import FastAPI, Body
from pydantic import BaseModel

import tensorflow as tf
import numpy as np

# 모델 불러오기
load = tf.saved_model.load('mnist/1')
load_inference = load.signatures["serving_default"]

app = FastAPI()

# class Payload(BaseModel):
#     data : str = ""

@app.get("/")
def root():
    return {"Prediction" : "Model!!!!"}

@app.post("/predict")
def inference(data : dict = Body(...)):
    result = load_inference(tf.constant(data['images'], dtype=tf.float32)/255.0)

    return str(np.argmax(result['dense_1'].numpy()))
    




