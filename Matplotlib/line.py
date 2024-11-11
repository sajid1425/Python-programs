import matplotlib.pyplot as plt
x = [1, 2, 3, 4]  
y = [1, 4, 9, 16]
plt.plot(x, y, label="y = x^2")
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Simple Line Plot")
plt.legend()
plt.show()