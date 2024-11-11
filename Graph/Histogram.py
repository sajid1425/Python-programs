# Import the necessary library for plotting
import matplotlib.pyplot as plt

# Define the data for the histogram
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]  # The list of data points

# Create the histogram with 5 bins and set the color of the bars to green
plt.hist(data, bins=5, color='green')

# Set the title of the histogram
plt.title("Histogram")

# Display the plot on the screen
plt.show()