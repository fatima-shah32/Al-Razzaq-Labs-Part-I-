import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import graphviz

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

print("=== Lab 12: Decision Tree Basics ===")

# Task 1: Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("\nDataset loaded successfully")
print("Feature shape:", X.shape)
print("Target shape:", y.shape)
print("Target classes:", iris.target_names)

# Train Decision Tree model
clf = DecisionTreeClassifier(random_state=0)
clf.fit(X, y)

accuracy = clf.score(X, y)

print("\nModel Accuracy:")
print(f"{accuracy:.2f}")

# Task 2: Text-based tree visualization
text_representation = tree.export_text(
    clf,
    feature_names=iris.feature_names
)

print("\nDecision Tree Text Representation:")
print(text_representation)

with open("decision_tree_text.txt", "w") as file:
    file.write(text_representation)

print("\nText tree saved as decision_tree_text.txt")

# Graphviz tree visualization
dot_data = tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True,
    special_characters=True
)

graph = graphviz.Source(dot_data)
graph.render("iris_tree", format="png", cleanup=True)

print("Graphviz tree saved as iris_tree.png")

# Matplotlib tree visualization
plt.figure(figsize=(16, 10))
tree.plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True
)
plt.title("Decision Tree Visualization")
plt.tight_layout()
plt.savefig("decision_tree_plot.png")
plt.close()

print("Matplotlib tree saved as decision_tree_plot.png")

# Task 3: Feature Importance
feature_importances = clf.feature_importances_

importance_df = pd.DataFrame({
    "Feature": iris.feature_names,
    "Importance": feature_importances
})

print("\nFeature Importances:")
print(importance_df)

importance_df.to_csv("feature_importances.csv", index=False)

# Plot feature importance
plt.figure(figsize=(8, 5))
plt.bar(
    importance_df["Feature"],
    importance_df["Importance"]
)
plt.xlabel("Features")
plt.ylabel("Importance")
plt.title("Decision Tree Feature Importances")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("feature_importance_plot.png")
plt.close()

print("Feature importances saved as feature_importances.csv")
print("Feature importance plot saved as feature_importance_plot.png")

print("\nLab completed successfully.")
