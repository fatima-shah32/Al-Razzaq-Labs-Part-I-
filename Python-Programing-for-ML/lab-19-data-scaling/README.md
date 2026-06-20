# Lab 19: Data Preprocessing with scikit-learn - Scaling

## Objective

Learn how to scale numerical data using StandardScaler from scikit-learn.

## Tools Used

- Python
- NumPy
- Pandas
- Scikit-learn
- Matplotlib

## Tasks Performed

1. Created a sample dataset
2. Imported StandardScaler
3. Scaled the dataset
4. Compared original and scaled statistics
5. Visualized original and scaled data

## Main Code

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df)
```

## Files Created

```text
original_data.png
scaled_data.png
```

## Final Structure

```text
lab-19-data-scaling/
├── README.md
├── data_scaling.py
├── original_data.png
├── scaled_data.png
└── ml-env/
```

## Conclusion

In this lab, I learned how to standardize numerical features using StandardScaler. After scaling, the data had a mean close to 0 and a standard deviation close to 1, which helps many machine learning algorithms perform better.
