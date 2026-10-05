import pandas as pd

data = pd.read_csv("students.csv")

data.rename(
    columns={"Marks": "Score"},
    inplace=True
)

print("Dataset after renaming the column:")
print(data)