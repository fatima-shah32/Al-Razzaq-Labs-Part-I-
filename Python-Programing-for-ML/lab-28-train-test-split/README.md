# Lab 28: Splitting Data into Training and Testing Sets

## Objective

Learn how to split datasets into training and testing sets using scikit-learn.

## Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn

## Dataset

Iris dataset from scikit-learn.

## Tasks Performed

1. Loaded the Iris dataset
2. Split the dataset using train_test_split()
3. Used an 80/20 train-test ratio
4. Verified training and testing dimensions
5. Implemented stratified splitting
6. Compared training and testing sample sizes

## Main Code

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)
Training vs Testing Data
Training Data

Used to train the machine learning model.

Testing Data

Used to evaluate the model on unseen data.

Output

The program displays:

Dataset size
Training data shape
Testing data shape
Number of training samples
Number of testing samples
Final Structure
lab-28-train-test-split/
├── README.md
├── train_test_split_lab.py
└── ml-env/
Conclusion

In this lab, I learned how to divide data into training and testing sets using train_test_split(). Proper data splitting helps evaluate model performance fairly and reduces the risk of overfitting.
