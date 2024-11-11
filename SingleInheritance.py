# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Vehicle Brand: {self.brand}, Model: {self.model}")

# Derived class
class Car(Vehicle):
    def __init__(self, brand, model, fuel_type):
        super().__init__(brand, model)
        self.fuel_type = fuel_type

    def display_car_info(self):
        self.display_info()
        print(f"Fuel Type: {self.fuel_type}")

# Creating an object of the Car class
car1 = Car("Toyota", "Corolla", "Petrol")
car1.display_car_info()
