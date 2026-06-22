# Lab 14: Train-Test Split & Cross-Validation

## Objectives

- Understand train-test split
- Implement k-fold cross-validation
- Compare model evaluation methods
- Understand why cross-validation gives stable results

## Tools Used

- Python
- Pandas
- Scikit-learn

## Dataset

Iris dataset from scikit-learn.

## Tasks Performed

1. Loaded Iris dataset
2. Created DataFrame
3. Split data using train_test_split
4. Trained LogisticRegression model
5. Performed 5-fold cross-validation
6. Compared train-test score with cross-validation mean score
7. Saved results and summary

## Files

```text
train_test_cross_validation.py
evaluation_results.csv
evaluation_summary.txt
README.md
Conclusion

This lab explained how train-test split and cross-validation are used for model evaluation. Train-test split gives one score, while cross-validation provides a more reliable estimate using multiple data splits.
