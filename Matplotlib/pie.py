import matplotlib.pyplot as plt
labels = ['Java', 'Python', 'C/C++', 'C#']
sizes = [15, 30, 45, 10]
plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()