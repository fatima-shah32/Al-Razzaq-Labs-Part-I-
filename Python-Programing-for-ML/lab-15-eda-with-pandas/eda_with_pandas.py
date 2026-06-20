import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_iris

print("=== Lab 15: Exploratory Data Analysis with Pandas ===")

# Load Iris dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["target"] = iris.target

print("\nDataset loaded successfully")

# Task 1: Generate Summary Statistics
print("\nFirst five rows:")
print(df.head())

print("\nDataset information:")
print(df.info())

print("\nSummary statistics:")
print(df.describe())

# Task 2: Identify Trends and Patterns
print("\nMissing values:")
print(df.isnull().sum())

# Fill missing values if any
df.fillna(df.mean(), inplace=True)

print("\nMissing values after handling:")
print(df.isnull().sum())

# Correlation analysis
correlation_matrix = df.corr()

print("\nCorrelation matrix:")
print(correlation_matrix)

# Save correlation heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
)
plt.title("Correlation Matrix Heatmap")
plt.tight_layout()
plt.savefig("correlation_heatmap.png")
plt.close()

print("\nCorrelation heatmap saved as correlation_heatmap.png")

# Task 3: Visualize Data Distributions

# Histogram
df["sepal length (cm)"].hist()
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("sepal_length_histogram.png")
plt.close()

print("Histogram saved as sepal_length_histogram.png")

# Boxplot
df.boxplot(
    column=[
        "sepal length (cm)",
        "sepal width (cm)"
    ]
)
plt.title("Boxplot of Sepal Length and Sepal Width")
plt.tight_layout()
plt.savefig("boxplot_sepal_features.png")
plt.close()

print("Boxplot saved as boxplot_sepal_features.png")

print("\nEDA lab completed successfully.")
