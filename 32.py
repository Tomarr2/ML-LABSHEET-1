# Q32: Load a dataset directly from Scikit-learn

import pandas as pd
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Create DataFrame using the dataset values
iris_data = pd.DataFrame(
    iris[0],
    columns=[
        "sepal_length",
        "sepal_width",
        "petal_length",
        "petal_width"
    ]
)

# Add target column
iris_data["target"] = iris[1]

print("First Five Records of Iris Dataset:")
print(iris_data.head())