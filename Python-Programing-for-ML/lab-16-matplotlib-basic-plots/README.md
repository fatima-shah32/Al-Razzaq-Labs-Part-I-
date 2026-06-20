# Lab 16: Data Visualization with Matplotlib - Basic Plots

## Objective

Learn how to create and customize basic plots using Matplotlib.

## Tools Used

- Python
- NumPy
- Matplotlib

## Tasks Performed

1. Created a line graph
2. Created a bar chart
3. Created a scatter plot
4. Added titles and axis labels
5. Saved plots as image files

## Main Code

```python
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y)
```

```python
plt.bar(categories, values)
```

```python
plt.scatter(x_scatter, y_scatter)
```

## Files Created

```text
line_graph.png
bar_chart.png
scatter_plot.png
```

## Final Structure

```text
lab-16-matplotlib-basic-plots/
├── README.md
├── basic_plots.py
├── line_graph.png
├── bar_chart.png
├── scatter_plot.png
└── ml-env/
```

## Conclusion

In this lab, I learned how to create line graphs, bar charts, and scatter plots using Matplotlib. I also customized plots with titles and axis labels to improve readability and presentation.
