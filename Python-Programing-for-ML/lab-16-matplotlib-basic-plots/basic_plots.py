import matplotlib.pyplot as plt
import numpy as np

print("=== Lab 16: Basic Plots with Matplotlib ===")

# Task 1: Line Graph
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)

plt.savefig("line_graph.png")
plt.close()

print("Line graph saved as line_graph.png")

# Task 2: Bar Chart
categories = ["A", "B", "C", "D"]
values = [4, 7, 1, 8]

plt.figure(figsize=(8, 5))
plt.bar(categories, values)

plt.title("Category Values")
plt.xlabel("Categories")
plt.ylabel("Values")

plt.savefig("bar_chart.png")
plt.close()

print("Bar chart saved as bar_chart.png")

# Task 3: Scatter Plot
x_scatter = np.random.rand(50)
y_scatter = np.random.rand(50)

plt.figure(figsize=(8, 5))
plt.scatter(x_scatter, y_scatter)

plt.title("Scatter Plot Example")
plt.xlabel("X Values")
plt.ylabel("Y Values")

plt.savefig("scatter_plot.png")
plt.close()

print("Scatter plot saved as scatter_plot.png")

print("\nLab completed successfully.")
