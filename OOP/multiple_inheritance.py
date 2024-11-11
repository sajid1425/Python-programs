class ClassA:
    def method_a(self):
        print("Method from Class A")

class ClassB:
    def method_b(self):
        print("Method from Class B")

class ClassC(ClassA, ClassB):
    def method_c(self):
        print("Method from Class C")

obj = ClassC()

obj.method_a()
obj.method_b() 
obj.method_c() 
