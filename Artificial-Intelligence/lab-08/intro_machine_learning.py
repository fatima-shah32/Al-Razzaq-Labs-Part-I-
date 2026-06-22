from sklearn.datasets import load_iris, make_blobs
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

print("=== Lab 08: Intro to Machine Learning Concepts ===")

# --------------------------------------------------
# Task 1 & 2: Supervised Learning Example (k-NN)
# --------------------------------------------------

print("\n--- Supervised Learning: Classification ---")

iris = load_iris()
X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

y_pred = knn.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)

print(f"Classification Accuracy: {accuracy:.2f}")

# --------------------------------------------------
# Task 2: Unsupervised Learning Example (K-Means)
# --------------------------------------------------

print("\n--- Unsupervised Learning: Clustering ---")

X_blob, y_blob = make_blobs(
    n_samples=300,
    centers=4,
    cluster_std=0.60,
    random_state=0
)

kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)

clusters = kmeans.fit_predict(X_blob)

plt.figure(figsize=(7, 5))
plt.scatter(X_blob[:, 0], X_blob[:, 1], c=clusters)
plt.scatter(
    kmeans.cluster_centers_[:, 0],
    kmeans.cluster_centers_[:, 1],
    marker='X',
    s=200
)
plt.title("K-Means Clustering")
plt.savefig("kmeans_clustering.png")
plt.show()

# --------------------------------------------------
# Task 3: Short Note
# --------------------------------------------------

print("\n--- Short Note ---")
print("""
Supervised Learning:
Used when labeled data is available and the goal is prediction
or classification. Examples include spam detection, disease
prediction, and house price forecasting.

Unsupervised Learning:
Used when labels are unavailable and the goal is to discover
hidden patterns or groups in data. Examples include customer
segmentation, anomaly detection, and clustering.
""")

print("Lab completed successfully.")
