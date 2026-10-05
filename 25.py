import pandas as pd

data = pd.read_csv("students.csv")

selected_data = data.iloc[0:5, 0:3]

print("Selected Data using iloc[]:")
print(selected_data)