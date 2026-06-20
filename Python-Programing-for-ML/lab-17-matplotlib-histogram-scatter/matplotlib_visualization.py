import numpy as np
import matplotlib.pyplot as plt

print("=== Lab 17: Histograms and Scatter Plots ===")

# Generate sample data for histogram
data = np.random.normal(
    loc=0,
    scale=1,
    size=1000
)

# Create Histogram
plt.figure(figsize=(10, 6))

plt.hist(
    data,
    bins=30,
    alpha=0.7,
    color="blue"
)

plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.grid(True)

plt.savefig("histogram_plot.png")
plt.close()

print("Histogram saved as histogram_plot.png")

# Generate sample data for scatter plot
x = np.random.rand(100)
y = x + np.random.normal(
    0,
    0.1,
    100
)

# Create Scatter Plot
plt.figure(figsize=(10, 6))

plt.scatter(
    x,
    y,
    c="red",
    marker="o",
    alpha=0.5
)

plt.title("Scatter Plot of Random Data")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.grid(True)

plt.savefig("scatter_plot.png")
plt.close()

print("Scatter plot saved as scatter_plot.png")

# Create Annotated Scatter Plot
plt.figure(figsize=(10, 6))

plt.scatter(
    x,
    y,
    c="green",
    marker="x"
)

plt.title("Annotated Scatter Plot")
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")

index = 10

plt.annotate(
    "Special Point",
    xy=(x[index], y[index]),
    xytext=(x[index] + 0.1, y[index] - 0.1),
    arrowprops=dict(
        facecolor="black",
        shrink=0.05
    )
)

plt.grid(True)

plt.savefig("annotated_scatter_plot.png")
plt.close()

print("Annotated scatter plot saved as annotated_scatter_plot.png")

print("\nLab completed successfully.")

