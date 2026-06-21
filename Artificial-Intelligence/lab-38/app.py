import pickle
import numpy as np
from flask import Flask, request

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return """
    <h2>Flask Model Deployment</h2>
    <p>Enter 4 Iris feature values separated by commas.</p>
    <form action="/predict-form" method="post">
        <input type="text" name="input_data" placeholder="5.1,3.5,1.4,0.2">
        <input type="submit" value="Predict">
    </form>
    """

@app.route("/predict-form", methods=["POST"])
def predict_form():
    data = request.form["input_data"]

    input_data = np.array([
        float(x.strip()) for x in data.split(",")
    ]).reshape(1, -1)

    prediction = model.predict(input_data)

    return f"<h3>Prediction Class: {prediction[0]}</h3><a href='/'>Go Back</a>"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["input"]
    input_data = np.array(data).reshape(1, -1)
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
