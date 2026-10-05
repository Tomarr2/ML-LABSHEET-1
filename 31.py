import pandas as pd

data = pd.read_csv("students.csv")

data["Result"] = data["Marks"].apply(lambda marks: "Pass" if marks >= 40 else "Fail")

data.to_csv("modified_students.csv",index=False)

print("Modified dataset saved successfully.")
print("File name: modified_students.csv")