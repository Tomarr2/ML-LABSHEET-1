# Q33: Create a histogram for a numerical feature

import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
iris = load_iris()

# Get dataset values
iris_values = iris[0]

# Select sepal length
sepal_length = iris_values[:, 0]

# Create histogram
plt.hist(sepal_length, bins=10)

plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.title("Histogram of Sepal Length")

plt.show()