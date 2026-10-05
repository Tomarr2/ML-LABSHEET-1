import pandas as pd

data = pd.read_csv("students.csv")

sorted_data = data.sort_values(by="Marks",ascending=False)

print("Dataset sorted by Marks:")
print(sorted_data)