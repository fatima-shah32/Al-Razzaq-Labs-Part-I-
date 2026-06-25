from flask import Flask, jsonify, request
import joblib

app = Flask(__name__)

model = joblib.load("model.pkl")

class_names = [
    "setosa",
    "versicolor",
    "virginica"
]

@app.route("/")
def home():
    return "Welcome to the Simple API for Inference!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)

        input_data = data["input"]

        prediction = model.predict([input_data])[0]

        return jsonify({
            "prediction": int(prediction),
            "class_name": class_names[int(prediction)]
        })

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 400

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
