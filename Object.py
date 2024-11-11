class Car:
    # Constructor
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    # Method to display car info
    def display_info(self):
        print(f"Car: {self.year} {self.make} {self.model}")

    # Method to start the car
    def start(self):
        print(f"The {self.make} {self.model} is starting.")

# Creating an object of the Car class
my_car = Car("Toyota", "Corolla", 2022)

# Calling the methods to display info and start the car
my_car.display_info()
my_car.start()
