import pandas as pd

data = pd.read_csv("students.csv")

print("Records before removing duplicates:")
print(len(data))

data = data.drop_duplicates()

print("Records after removing duplicates:")
print(len(data))

print("\nDataset:")
print(data)