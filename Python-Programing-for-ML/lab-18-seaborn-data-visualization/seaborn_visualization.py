import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

print("=== Lab 18: Seaborn Data Visualization ===")

# Load sample dataset
tips = sns.load_dataset("tips")

print("\nDataset Preview:")
print(tips.head())

print("\nDataset Shape:")
print(tips.shape)

# Set theme and palette
sns.set_theme(style="whitegrid")
sns.set_palette("pastel")

# Box Plot
plt.figure(figsize=(8, 6))

sns.boxplot(
    x="day",
    y="total_bill",
    data=tips
)

plt.title("Box Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")

plt.tight_layout()
plt.savefig("boxplot_total_bill.png")
plt.close()

print("Box plot saved as boxplot_total_bill.png")

# Violin Plot
plt.figure(figsize=(8, 6))

sns.violinplot(
    x="day",
    y="total_bill",
    data=tips,
    inner="quartile"
)

plt.title("Violin Plot of Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Total Bill ($)")

plt.tight_layout()
plt.savefig("violinplot_total_bill.png")
plt.close()

print("Violin plot saved as violinplot_total_bill.png")

# Customized Box Plot
plt.figure(figsize=(8, 6))

sns.boxplot(
    x="day",
    y="total_bill",
    data=tips
)

plt.title("Customized Box Plot of Total Bill by Day")
plt.xlabel("Day of the Week")
plt.ylabel("Total Bill ($)")

plt.tight_layout()
plt.savefig("custom_boxplot.png")
plt.close()

print("Customized box plot saved as custom_boxplot.png")

print("\nLab completed successfully.")
