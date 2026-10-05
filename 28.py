import pandas as pd

data = pd.read_csv("students.csv")

data["Result"] = data["Marks"].apply(lambda marks: "Pass" if marks >= 40 else "Fail")

print("Dataset after adding Result column:")
print(data)