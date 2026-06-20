# Lab 18: Introduction to Seaborn for ML Data Visualization

## Objective

Learn how to create box plots and violin plots using Seaborn and customize plot aesthetics.

## Tools Used

- Python
- Pandas
- Matplotlib
- Seaborn

## Dataset

Built-in **tips** dataset from Seaborn.

## Tasks Performed

1. Installed and imported Seaborn
2. Loaded the tips dataset
3. Created a box plot
4. Created a violin plot
5. Applied themes and color palettes
6. Customized plot titles and labels

## Main Code

```python
tips = sns.load_dataset("tips")
```

```python
sns.boxplot(
    x="day",
    y="total_bill",
    data=tips
)
```

```python
sns.violinplot(
    x="day",
    y="total_bill",
    data=tips,
    inner="quartile"
)
```

## Files Created

```text
boxplot_total_bill.png
violinplot_total_bill.png
custom_boxplot.png
```

## Final Structure

```text
lab-18-seaborn-data-visualization/
├── README.md
├── seaborn_visualization.py
├── boxplot_total_bill.png
├── violinplot_total_bill.png
├── custom_boxplot.png
└── ml-env/
```

## Conclusion

In this lab, I learned how to use Seaborn for statistical data visualization. I created box plots and violin plots, applied themes and color palettes, and customized plot labels to make visualizations more informative and attractive.
