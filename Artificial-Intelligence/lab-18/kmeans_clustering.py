import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

print("=== Lab 18: Intro to Clustering K-Means ===")

# Task 1: Generate sample dataset
X, _ = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=0.60,
    random_state=0
)

print("\nSample dataset generated successfully")
print("Dataset shape:", X.shape)

# Save dataset
dataset_df = pd.DataFrame(X, columns=["Feature_1", "Feature_2"])
dataset_df.to_csv("sample_cluster_dataset.csv", index=False)

# Visualize sample dataset
plt.figure(figsize=(8, 5))
plt.scatter(X[:, 0], X[:, 1], s=50)
plt.title("Sample Dataset Visualization")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.tight_layout()
plt.savefig("sample_dataset.png")
plt.close()

print("Sample dataset plot saved as sample_dataset.png")

# Task 2: Elbow Method
inertia = []

for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i,
        random_state=0,
        n_init=10
    )

    kmeans.fit(X)

    inertia.append(kmeans.inertia_)

print("\nInertia values for Elbow Method:")
for k, value in zip(range(1, 11), inertia):
    print(f"k={k}, inertia={value:.2f}")

# Save elbow values
elbow_df = pd.DataFrame({
    "k": list(range(1, 11)),
    "inertia": inertia
})

elbow_df.to_csv("elbow_method_values.csv", index=False)

# Plot elbow method
plt.figure(figsize=(8, 5))
plt.plot(range(1, 11), inertia, marker="o")
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")
plt.grid(True)
plt.tight_layout()
plt.savefig("elbow_method.png")
plt.close()

print("Elbow method plot saved as elbow_method.png")

# Task 3: Apply K-Means with k=4
kmeans = KMeans(
    n_clusters=4,
    random_state=0,
    n_init=10
)

y_kmeans = kmeans.fit_predict(X)

print("\nK-Means clustering applied successfully")

# Save clustered data
clustered_df = pd.DataFrame({
    "Feature_1": X[:, 0],
    "Feature_2": X[:, 1],
    "Cluster": y_kmeans
})

clustered_df.to_csv("clustered_data.csv", index=False)

print("Clustered data saved as clustered_data.csv")

# Visualize clusters
plt.figure(figsize=(8, 6))

for cluster in range(4):
    plt.scatter(
        X[y_kmeans == cluster, 0],
        X[y_kmeans == cluster, 1],
        s=50,
        label=f"Cluster {cluster + 1}"
    )

plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    s=300,
    marker="X",
    label="Centroids"
)

plt.title("K-Means Clustering Visualization")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.legend()
plt.tight_layout()
plt.savefig("kmeans_clusters.png")
plt.close()

print("Cluster visualization saved as kmeans_clusters.png")

# Save report
with open("clustering_report.txt", "w") as file:
    file.write("Lab 18: Intro to Clustering K-Means\n\n")
    file.write("Dataset: Synthetic dataset generated using make_blobs\n")
    file.write("Number of samples: 300\n")
    file.write("Selected number of clusters: 4\n\n")

    file.write("Elbow Method Inertia Values:\n")
    for k, value in zip(range(1, 11), inertia):
        file.write(f"k={k}, inertia={value:.2f}\n")

    file.write("\nInterpretation:\n")
    file.write("K-Means grouped the data into 4 clusters based on distance.\n")
    file.write("Centroids represent the center point of each cluster.\n")
    file.write("The elbow method helps choose a suitable value of k.\n")

print("Report saved as clustering_report.txt")

print("\nLab completed successfully.")
