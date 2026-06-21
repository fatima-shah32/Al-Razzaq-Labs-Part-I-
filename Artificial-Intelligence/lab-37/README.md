# Lab 37: Simple Dimensionality Reduction PCA

## Objective

Apply Principal Component Analysis to reduce dataset dimensions and train a classifier on reduced features.

## Dataset

Iris dataset from scikit-learn.

## Tools Used

- Python
- NumPy
- Pandas
- Matplotlib
- Scikit-learn

## Tasks Performed

1. Loaded Iris dataset
2. Standardized features using StandardScaler
3. Applied PCA
4. Checked explained variance ratio
5. Selected top 2 principal components
6. Trained Logistic Regression model
7. Evaluated model accuracy
8. Saved plots and reduced dataset

## Files Created

```text
explained_variance.png
pca_scatter_plot.png
pca_reduced_data.csv
Final Structure
Artificial-Intelligence/
└── lab-37/
    ├── README.md
    ├── pca_dimensionality_reduction.py
    ├── explained_variance.png
    ├── pca_scatter_plot.png
    ├── pca_reduced_data.csv
    └── ai-env/
Conclusion

In this lab, I learned how PCA reduces dimensionality while keeping important information. I standardized the Iris dataset, applied PCA, selected two components, trained a Logistic Regression model, and evaluated its accuracy.
