# Import the necessary library for plotting
import matplotlib.pyplot as plt

# Define the data for the pie chart
labels = ['Apples', 'Bananas', 'Cherries', 'Dates']  # The labels for each slice of the pie
sizes = [15, 30, 45, 10]  # The sizes (proportions) of each slice

# Create the pie chart with labels and percentage values
# autopct='%1.1f%%' formats the percentage to show one decimal place
plt.pie(sizes, labels=labels, autopct='%1.1f%%')

# Set the title of the pie chart
plt.title("Pie Chart")

# Display the pie chart
plt.show()