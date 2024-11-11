# Base class 1
class Flyable:
    def fly(self):
        print("Can fly")

# Base class 2
class Swimmable:
    def swim(self):
        print("Can swim")

# Derived class
class Duck(Flyable, Swimmable):
    def quack(self):
        print("Duck quacks")

# Creating an object of the Duck class
duck1 = Duck()
duck1.fly()
duck1.swim()
duck1.quack()
