from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np
import json



# Load trained model
model = pickle.load(open("models/final_model.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # get features from request form
    mileage = np.log10(float(request.form["mileage"]))
    mpg = float(request.form["mpg"])
    engineSize = float(request.form["engineSize"])
    age = 2021 - float(request.form["year"])
    brand = float(request.form["brand"])
    transmission = float(request.form["transmission"])
    new_data = np.array([mileage, mpg, engineSize, age, brand, transmission])

    # prediction
    prediction = model.predict(new_data.reshape(1, 6))
    output = round(prediction[0], 2)

    return render_template("index.html", prediction_text="Car price should be $ {}".format(output))
        
@app.route("/predict-api", methods=["POST"])
def predict_api():
    '''
    For direct API calls through request
    '''
    request_json = request.get_json()
    new_data = [float(x) for x in request_json["input"]]
    features = np.array(new_data)

    # prediction
    prediction = model.predict(features.reshape(1, 6))
    output = prediction[0]
    
    response = json.dumps({'response': str(output)})
    return response, 200


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5000)
    app.run(debug=True)




