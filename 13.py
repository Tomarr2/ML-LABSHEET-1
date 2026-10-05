import pandas as pd

data = pd.read_csv("students.csv")

print("Last Five Records:")
print(data.tail())