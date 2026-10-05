import pandas as pd

data = pd.read_csv("students.csv")

print("Gender Frequency:")
print(data["Gender"].value_counts())