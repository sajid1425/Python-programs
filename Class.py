class Bus:
    # Constructor
    def __init__(self, route, capacity):
        self.route = route
        self.capacity = capacity

    # Method to display route info
    def display_info(self):
        print(f"Route: {self.route}, Capacity: {self.capacity}")

# Creating an object of the Bus class
bus1 = Bus("Route 10", 50)

# Calling the display_info method to print the route info
bus1.display_info()
