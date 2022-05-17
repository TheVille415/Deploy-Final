# Importing Necessary modules
from fastapi import FastAPI
from tensorflow.keras.models import load_model
from tensorflow.keras.utils import get_file 
from tensorflow.keras.utils import load_img 
from tensorflow.keras.utils import img_to_array
from tensorflow import expand_dims
from tensorflow.nn import softmax
from tensorflow import keras
from numpy import argmax
from numpy import max
from numpy import array
from json import dumps
from uvicorn import run
import tensorflow as tf
import os

# Declaring our FastAPI instance
app = FastAPI()
# model_dir = "dnn_pricing_model.h5"
# model = load_model(model_dir)

# creating the BaseModel ,in pydantic aka our Request Body
# class request_body(BaseModel):
#     sepal_length : float
#     sepal_width : float
#     petal_length : float
#     petal_width : float
    
# Defining path operation for root endpoint
@app.get('/')
def main():
	return {'message': 'Welcome to GeeksforGeeks!'}

# Defining path operation for /name endpoint
@app.get('/{name}')
def hello_name(name : str):
	# Defining a function that takes only string as input and output the
	# following message.
	return {'message': f'Welcome to GeeksforGeeks!, {name}'}

@app.post('/predict/')
def ValuePredictor(Housing_size : int):
    """Return first index of result once loading model."""
    model = keras.models.load_model(
        "dnn_pricing_model"
    )
    # # keras .predict() methods expect batch of inputs, so let's provide an axis
    # # to avoid errors
    prediction_input = tf.expand_dims(int(Housing_size), axis=0)
    prediction = model.predict(prediction_input)
    # print(f"prediction: {prediction}")
    # return prediction
    return prediction