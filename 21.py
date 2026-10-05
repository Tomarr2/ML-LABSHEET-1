import pandas as pd

data = pd.read_csv("students.csv")

print("Unique Gender Values:")
print(data["Gender"].unique())