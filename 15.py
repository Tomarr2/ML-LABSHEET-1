import pandas as pd

data = pd.read_csv("students.csv")

print("Column Names:")

for column in data.columns:
    print(column)