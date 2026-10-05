import pandas as pd

data = pd.read_csv("students.csv")

print("Missing Values Count:")
print(data.isnull().sum())