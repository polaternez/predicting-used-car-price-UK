from hashlib import new
import json
from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np


app = Flask(__name__)
model = pickle.load(open("models/final_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    brand = float(request.form["brand"])
    transmission = float(request.form["transmission"])
    age = 2021 - float(request.form["year"])
    mileage = np.log10(float(request.form["mileage"]))
    mpg = float(request.form["mpg"])
    engineSize = float(request.form["engineSize"])
    new_data = np.array([mileage, mpg, engineSize, age, brand, transmission])

    prediction = model.predict(new_data.reshape(1, 6))
    output = round(prediction[0], 2)

    return render_template("index.html", prediction_text="Car price should be $ {}".format(output))
        
@app.route("/predict_api", methods=["POST"])
def predict_api():
    '''
    For direct API calls trought request
    '''
    request_json = request.get_json()
    new_data = [float(x) for x in request_json["input"]]
    features = np.array(new_data)
    prediction = model.predict(features.reshape(1, 6))
    output = prediction[0]
    
    response = json.dumps({'response': str(output)})
    return response, 200

if __name__ == "__main__":
    app.run(debug=True)


