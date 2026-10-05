import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [10, 20, 15, 30, 25]

plt.plot(x_values, y_values, marker="o")

plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Simple Line Plot")

plt.show()