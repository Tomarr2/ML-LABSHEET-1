import pandas as pd

data = pd.read_csv("students.csv")

selected_data = data.loc[
    0:4,
    ["Name", "Course", "Marks"]
]

print("Selected Data using loc[]:")
print(selected_data)