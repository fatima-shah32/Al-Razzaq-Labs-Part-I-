# Lab 27: Visualizing Decision Trees

## Objective

Learn how to train and visualize a Decision Tree model using scikit-learn, matplotlib, and graphviz.

## Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib
- Graphviz

## Dataset

Iris dataset from scikit-learn.

## Tasks Performed

1. Loaded the Iris dataset
2. Trained a DecisionTreeClassifier
3. Visualized the tree using matplotlib
4. Exported the tree using graphviz
5. Saved decision tree diagrams as PNG files
6. Interpreted tree structure

## Main Code

```python
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)
tree.plot_tree(
    clf,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)
dot_data = tree.export_graphviz(
    clf,
    out_file=None,
    feature_names=iris.feature_names,
    class_names=iris.target_names,
    filled=True,
    rounded=True
)
Files Created
decision_tree_plot.png
iris_decision_tree.png
Tree Interpretation
Internal nodes show feature-based decisions
Leaf nodes show final predicted classes
Gini value shows impurity
Lower Gini means better split
Tree depth shows model complexity
Final Structure
lab-27-visualizing-decision-trees/
├── README.md
├── decision_tree_visualization.py
├── decision_tree_plot.png
├── iris_decision_tree.png
└── ml-env/
Conclusion

In this lab, I learned how to visualize Decision Tree models. I trained a DecisionTreeClassifier on the Iris dataset and created tree diagrams using matplotlib and graphviz. This helped me understand how decision trees make predictions using feature splits.
