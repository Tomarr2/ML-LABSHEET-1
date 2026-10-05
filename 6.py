import seaborn as sns
import matplotlib.pyplot as plt

values = [10, 20, 15, 30, 25, 35, 40]

sns.histplot(values, kde=True)

plt.xlabel("Values")
plt.ylabel("Frequency")
plt.title("Basic Statistical Plot")

plt.show()