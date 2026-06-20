import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import graphviz

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree


print("=== Lab 27: Visualizing Decision Trees ===")

# Load Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

print("\nDataset loaded successfully")
print("Feature names:", iris.feature_names)
print("Class names:", iris.target_names)
print("Feature shape:", X.shape)
print("Target shape:", y.shape)

# Train Decision Tree model
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

print("\nDecision Tree model trained successfully")

# Visualize using matplotlib
plt.figure(figsize=(15, 10))

tree.plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)

plt.title("Decision Tree Visualization - Iris Dataset")
plt.savefig("decision_tree_plot.png")
plt.close()

print("Decision tree image saved as decision_tree_plot.png")

# Export tree using graphviz
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

# Save graphviz output
graph.render("iris_decision_tree", format="png", cleanup=True)

print("Graphviz decision tree saved as iris_decision_tree.png")

print("\nInterpretation:")
print("Each internal node shows a feature-based decision.")
print("Leaf nodes show the final predicted class.")
print("Gini value shows impurity of the split.")
print("Lower Gini means better class separation.")
print("Tree depth shows model complexity.")
