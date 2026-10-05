import pandas as pd

data = pd.read_csv("students.csv")

filtered_data = data[data["Marks"] > 80]

print("Students with Marks greater than 80:")
print(filtered_data)