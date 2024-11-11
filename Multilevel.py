# Base class
class Animal:
    def sound(self):
        print("Animal makes a sound")

# Intermediate class
class Mammal(Animal):
    def has_hair(self):
        print("Mammals have hair or fur")

# Derived class
class Dog(Mammal):
    def bark(self):
        print("Dog barks")

# Creating an object of the Dog class
dog1 = Dog()
dog1.sound()
dog1.has_hair()
dog1.bark()
