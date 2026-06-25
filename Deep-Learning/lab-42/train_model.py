import joblib

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("=== Training Model for API Inference ===")

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

joblib.dump(model, "model.pkl")

with open("model_report.txt", "w") as file:
    file.write("Simple API Inference Model Report\n\n")
    file.write("Dataset: Iris\n")
    file.write("Model: RandomForestClassifier\n")
    file.write(f"Accuracy: {accuracy:.2f}\n")

print("Model saved as model.pkl")
print(f"Model Accuracy: {accuracy:.2f}")
