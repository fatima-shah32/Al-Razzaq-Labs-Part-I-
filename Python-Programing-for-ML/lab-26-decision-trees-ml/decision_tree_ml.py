import pandas as pd
import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.metrics import accuracy_score


print("=== Lab 26: Introduction to Decision Trees for ML ===")

# Load Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

print("\nDataset loaded successfully")
print("Feature names:", iris.feature_names)
print("Target names:", iris.target_names)
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data shape:", X_train.shape)
print("Testing data shape:", X_test.shape)

# Train Decision Tree using Gini criterion
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

print("\nDecision Tree model trained successfully")

# Predict and evaluate model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print("Decision Tree Accuracy:", round(accuracy, 2))

# Export tree rules as text
tree_rules = export_text(
    clf,
    feature_names=iris.feature_names
)

print("\nDecision Tree Rules:")
print(tree_rules)

# Train Decision Tree using Entropy criterion
clf_entropy = DecisionTreeClassifier(
    criterion="entropy",
    random_state=42
)

clf_entropy.fit(X_train, y_train)

entropy_pred = clf_entropy.predict(X_test)
entropy_accuracy = accuracy_score(y_test, entropy_pred)

print("\nEntropy Decision Tree Accuracy:", round(entropy_accuracy, 2))

# Feature importance
importance = clf.feature_importances_

feature_importance_df = pd.DataFrame(
    importance,
    index=iris.feature_names,
    columns=["Importance"]
)

feature_importance_df = feature_importance_df.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(feature_importance_df)

feature_importance_df.to_csv("feature_importance.csv")

# Visualize the Decision Tree
plt.figure(figsize=(20, 10))

plot_tree(
    clf,
    filled=True,
    feature_names=iris.feature_names,
    class_names=iris.target_names
)

plt.title("Decision Tree Visualization - Iris Dataset")
plt.savefig("decision_tree_visualization.png")
plt.close()

print("\nDecision tree visualization saved as decision_tree_visualization.png")
print("Feature importance saved as feature_importance.csv")
