class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

# Creating objects of Dog and Cat
dog = Dog()
cat = Cat()

dog.sound()  # Outputs: Dog barks
cat.sound()  # Outputs: Cat meows
