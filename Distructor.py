class Bus:
    def __init__(self, route, capacity):
        self.route = route
        self.capacity = capacity
        print(f"Bus object for route {self.route} created.")

    def display_info(self):
        print(f"Route: {self.route}, Capacity: {self.capacity}")

    # Destructor
    def __del__(self):
        print(f"Bus object for route {self.route} is being destroyed.")

# Creating and deleting an object
bus2 = Bus("Route 20", 40)
bus2.display_info()

# Deleting bus2
del bus2
