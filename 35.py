# Q35: Generate a correlation matrix and visualize it using a heatmap

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Get dataset values
iris_values = iris[0]

# Create DataFrame
iris_data = pd.DataFrame(
    iris_values,
    columns=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)

# Calculate correlation matrix
correlation_matrix = iris_data.corr()

# Display matrix
print("Correlation Matrix:")
print(correlation_matrix)

#  heatmap
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix Heatmap")
plt.show()