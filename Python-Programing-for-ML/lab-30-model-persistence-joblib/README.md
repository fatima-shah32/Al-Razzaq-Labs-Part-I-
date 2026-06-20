# Lab 30: Introduction to Model Persistence with Joblib

## Objective

Learn how to save and load a trained machine learning model using Joblib.

## Tools Used

- Python
- NumPy
- Scikit-learn
- Joblib

## Dataset

Iris dataset from scikit-learn.

## Steps Performed

1. Loaded the Iris dataset
2. Split data into training and testing sets
3. Trained a RandomForestClassifier
4. Saved the trained model using Joblib
5. Loaded the saved model
6. Made predictions using the loaded model

## Main Code

```python
joblib.dump(model, "random_forest_model.pkl")

loaded_model = joblib.load("random_forest_model.pkl")
Output

The program prints:

Dataset shape
Model accuracy before saving
Saved model filename
Predicted labels
Actual labels
Loaded model accuracy
Files Created
random_forest_model.pkl
Final Structure
lab-30-model-persistence-joblib/
├── README.md
├── model_persistence_joblib.py
├── random_forest_model.pkl
└── ml-env/
Conclusion

In this lab, I learned model persistence using Joblib. I trained a Random Forest model, saved it as a .pkl file, loaded it again, and used it to make predictions without retraining.
