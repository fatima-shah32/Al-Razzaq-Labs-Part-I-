import matplotlib.pyplot as plt
import numpy as np

print("=== Lab 06: Basic Data Visualization ===")

# ----------------------------------
# Task 1: Line Plot
# ----------------------------------
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure(figsize=(6,4))
plt.plot(x, y, marker='o', label='Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Line Plot')
plt.legend()
plt.grid(True)
plt.savefig("line_plot.png")
plt.show()

# ----------------------------------
# Task 2: Bar Chart
# ----------------------------------
categories = ['A', 'B', 'C', 'D']
values = [4, 7, 1, 8]

plt.figure(figsize=(6,4))
plt.bar(categories, values, color='lightblue')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart Example')
plt.savefig("bar_chart.png")
plt.show()

# ----------------------------------
# Task 3: Histogram
# ----------------------------------
data = np.random.randn(1000)

plt.figure(figsize=(6,4))
plt.hist(data, bins=30, color='green', alpha=0.7)
plt.xlabel('Data')
plt.ylabel('Frequency')
plt.title('Histogram Example')
plt.savefig("histogram.png")
plt.show()

print("\nPlots created successfully.")
