# Import the necessary library for plotting
import matplotlib.pyplot as plt

# Define the data for the x and y values
x = [1, 2, 3, 4, 5]  # x values
y = [1, 4, 9, 16, 25]  # y values corresponding to y = x^2

# Plot the data with a label for the line
plt.plot(x, y, label="y = x^2")

# Set the x-axis label
plt.xlabel("x values")

# Set the y-axis label
plt.ylabel("y values")

# Set the title of the plot
plt.title("Simple Line Plot")

# Display the legend for the line label
plt.legend()

# Show the plot
plt.show()