import pandas as pd

data = pd.read_csv("students.csv")

rows, columns = data.shape

print("Total Rows:", rows)
print("Total Columns:", columns)