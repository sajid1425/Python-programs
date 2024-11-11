# Import the necessary library for plotting
import matplotlib.pyplot as plt

# Define the categories and values to be plotted
categories = ['A', 'B', 'C', 'D']  # List of categories (x-axis labels)
values = [5, 7, 3, 8]  # List of values corresponding to each category (y-axis values)

# Create a bar plot with categories on the x-axis and values on the y-axis
# The color of the bars is set to 'orange'
plt.bar(categories, values, color='orange')

# Set the title of the plot
plt.title("Bar Plot")

# Display the plot on the screen
plt.show()