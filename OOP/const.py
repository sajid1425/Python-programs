class Person:
    def __init__(self, name):
        self.name = name
        print(f"Constructor: {self.name} is created.")
    def __del__(self):
        print(f"Destructor: {self.name} is deleted.")
p1 = Person("Alice")
del p1
