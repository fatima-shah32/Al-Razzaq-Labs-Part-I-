# Lab 26: Introduction to Decision Trees for ML

## Objective

Understand, train, evaluate, and visualize a Decision Tree classifier using scikit-learn.

## Tools Used

- Python
- Pandas
- Scikit-learn
- Matplotlib

## Dataset

Iris dataset from scikit-learn.

## Tasks Performed

1. Loaded the Iris dataset
2. Split data into training and testing sets
3. Trained a DecisionTreeClassifier
4. Displayed decision tree rules using export_text
5. Compared Gini and Entropy split criteria
6. Checked feature importance
7. Visualized and saved the decision tree

## Main Code

```python
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
tree_rules = export_text(
    clf,
    feature_names=iris.feature_names
)
plot_tree(
    clf,
    filled=True,
    feature_names=iris.feature_names,
    class_names=iris.target_names
)
Files Created
decision_tree_visualization.png
feature_importance.csv
Final Structure
lab-26-decision-trees-ml/
├── README.md
├── decision_tree_ml.py
├── decision_tree_visualization.png
├── feature_importance.csv
└── ml-env/
Conclusion

In this lab, I learned how Decision Trees work in machine learning. I trained a DecisionTreeClassifier, displayed its decision rules, compared Gini and Entropy split criteria, checked feature importance, and saved a visual diagram of the tree.
