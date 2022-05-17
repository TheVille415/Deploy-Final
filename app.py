# Load libraries
import flask
import pandas as pd
import tensorflow as tf
import keras
from keras.models import load_model

# instantiate flask 
app = flask.Flask(__name__)

# load the model
model = load_model('dnn_pricing_model.h5')

# define a predict function as an endpoint 
@app.route("/predict", methods=["GET","POST"])
def predict():
    # return will jsonify the data to fill in the data we return
    data = {"success": False}

    # reads request
    params = flask.request.json
    if (params == None):
        params = flask.request.args

    # if parameters are found, return a prediction
    if (params != None):
        # is a single datapoint
        x=pd.DataFrame.from_dict(params, orient='index').transpose()
        with graph.as_default():
            data["prediction"] = str(model.predict(x)[0][0])
            data["success"] = True

    # return a response in json format 
    return flask.jsonify(data)    

# start the flask app, allow remote connections 
app.run(host='0.0.0.0')