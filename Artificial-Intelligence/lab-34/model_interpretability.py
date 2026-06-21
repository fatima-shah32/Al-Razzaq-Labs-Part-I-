import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import shap

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


print("=== Lab 34: Intro to Model Interpretability ===")

# Load Iris dataset
iris = load_iris()

X = iris.data
y = iris.target
feature_names = iris.feature_names

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Feature names:", feature_names)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

# Train Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully")

# Model accuracy
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", round(accuracy, 2))

# Feature importance from model
feature_importance = pd.DataFrame({
    "Feature": feature_names,
    "Importance": model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(feature_importance)

feature_importance.to_csv("feature_importance.csv", index=False)

# Plot feature importance
plt.figure(figsize=(8, 5))
plt.barh(
    feature_importance["Feature"],
    feature_importance["Importance"]
)
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.close()

print("\nFeature importance plot saved as feature_importance.png")

# SHAP explanation
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

print("\nSHAP values calculated successfully")

# SHAP summary plot
shap.summary_plot(
    shap_values,
    X_test,
    feature_names=feature_names,
    show=False
)

plt.tight_layout()
plt.savefig("shap_summary_plot.png")
plt.close()

print("SHAP summary plot saved as shap_summary_plot.png")

# Explain one sample prediction
sample_index = 0
sample_data = X_test[sample_index].reshape(1, -1)

prediction = model.predict(sample_data)

print("\nSample Prediction Explanation")
print("Sample Index:", sample_index)
print("Predicted Class:", iris.target_names[prediction[0]])
print("Actual Class:", iris.target_names[y_test[sample_index]])

# Save explanation text
with open("sample_prediction_explanation.txt", "w") as file:
    file.write("Lab 34: Model Interpretability\n\n")
    file.write("Model Used: RandomForestClassifier\n")
    file.write(f"Model Accuracy: {round(accuracy, 2)}\n\n")
    file.write("Sample Prediction Explanation\n")
    file.write(f"Sample Index: {sample_index}\n")
    file.write(f"Predicted Class: {iris.target_names[prediction[0]]}\n")
    file.write(f"Actual Class: {iris.target_names[y_test[sample_index]]}\n\n")
    file.write("Feature Importance:\n")
    file.write(feature_importance.to_string(index=False))
    file.write("\n\nSHAP explains how each feature contributes to model predictions.")

print("Sample explanation saved as sample_prediction_explanation.txt")

print("\nLab completed successfully.")
