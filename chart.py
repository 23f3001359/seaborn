# chart.py

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
segments = ['Budget', 'Regular', 'Premium', 'Luxury']
data = []

# Create realistic purchase distributions for each segment
for segment in segments:
    if segment == 'Budget':
        purchases = np.random.normal(loc=30, scale=10, size=200)
    elif segment == 'Regular':
        purchases = np.random.normal(loc=75, scale=20, size=200)
    elif segment == 'Premium':
        purchases = np.random.normal(loc=150, scale=30, size=200)
    else:  # Luxury
        purchases = np.random.normal(loc=300, scale=50, size=200)
    
    for amount in purchases:
        data.append({'Customer Segment': segment, 'Purchase Amount ($)': round(max(amount, 0), 2)})

df = pd.DataFrame(data)

# Set professional Seaborn styling
sns.set_style("whitegrid")
sns.set_context("talk")

# Create boxplot
plt.figure(figsize=(8, 8))  # 512x512 pixels when saved with dpi=64
sns.boxplot(
    x="Customer Segment",
    y="Purchase Amount ($)",
    data=df,
    palette="Set2"
)

# Add titles and labels
plt.title("Purchase Amount Distribution by Customer Segment", fontsize=16)
plt.xlabel("Customer Segment", fontsize=12)
plt.ylabel("Purchase Amount ($)", fontsize=12)

# Save the figure
plt.tight_layout()
plt.savefig("chart.png", dpi=64, bbox_inches='tight')
