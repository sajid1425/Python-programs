# Import the necessary library for plotting
import matplotlib.pyplot as plt

# Define the data for the x and y values
x = [1, 2, 3, 4, 5]  # x values (data points on the horizontal axis)
y = [1, 4, 9, 16, 25]  # y values corresponding to the x values (data points on the vertical axis)

# Create the scatter plot with blue color and circular markers
# 'o' specifies the marker style (circle), and 'color='blue'' sets the marker color
plt.scatter(x, y, color='blue', marker='o')

# Set the title of the scatter plot
plt.title("Scatter Plot")

# Display the plot
plt.show()