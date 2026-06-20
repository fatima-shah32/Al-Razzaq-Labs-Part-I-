# Lab 17: Data Visualization with Matplotlib - Histograms and Scatter Plots

## Objective

Learn how to create histograms, scatter plots, and annotated visualizations using Matplotlib.

## Tools Used

- Python
- NumPy
- Matplotlib

## Tasks Performed

1. Generated normally distributed data
2. Created a histogram
3. Generated random data for scatter plotting
4. Created a scatter plot
5. Added annotations to highlight a data point
6. Saved all visualizations as image files

## Main Code

```python
plt.hist(
    data,
    bins=30,
    alpha=0.7,
    color="blue"
)
```

```python
plt.scatter(
    x,
    y,
    c="red",
    marker="o",
    alpha=0.5
)
```

```python
plt.annotate(
    "Special Point",
    xy=(x[index], y[index])
)
```

## Files Created

```text
histogram_plot.png
scatter_plot.png
annotated_scatter_plot.png
```

## Final Structure

```text
lab-17-matplotlib-histogram-scatter/
├── README.md
├── matplotlib_visualization.py
├── histogram_plot.png
├── scatter_plot.png
├── annotated_scatter_plot.png
└── ml-env/
```

## Conclusion

In this lab, I learned how to visualize data using Matplotlib. I created histograms to understand data distribution, scatter plots to observe relationships between variables, and annotations to highlight important points in the visualization.
