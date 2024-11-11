class Laptop:
    # Constructor
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
        print(f"Laptop created: {self.brand} {self.model}, Price: ${self.price}")

    # Method to display laptop info
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}")

# Creating an object of the Laptop class
laptop1 = Laptop("Dell", "XPS 13", 1200)

# Calling the method to display laptop info
laptop1.display_info()
