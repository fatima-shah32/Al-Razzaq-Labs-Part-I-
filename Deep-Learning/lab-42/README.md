# Lab 42: Building a Simple API for Inference

## Objective

Build a simple RESTful API using Flask and serve predictions from a trained machine learning model.

## Tools Used

- Python
- Flask
- Scikit-learn
- Joblib
- NumPy

## Dataset

Iris dataset from scikit-learn.

## Workflow

1. Train RandomForestClassifier model
2. Save model using joblib
3. Build Flask API
4. Create `/predict` endpoint
5. Send sample JSON input
6. Return prediction response

## Files

```text
train_model.py
app.py
model.pkl
model_report.txt
sample_input.json
README.md

Conclusion

This lab demonstrated how to build a simple Flask API for machine learning inference. The trained model was saved using joblib and loaded inside the API to return real-time predictions.
