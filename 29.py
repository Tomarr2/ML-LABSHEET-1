import pandas as pd

data = pd.read_csv("students.csv")

data.drop("Gender",axis=1,inplace=True)

print("Dataset after deleting Gender column:")
print(data)