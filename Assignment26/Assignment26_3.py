# 3: Write a Python program to implement a class named Arithmetic with the following characteristics:
# •	The class should contain two instance variables: Value1 and Value2. 
# •	Define a constructor (__init__) that initializes all instance variables to 0. 
# •	Implement the following instance methods: 
# •	Accept() – accepts values for Value1 and Value2 from the user. 
# •	Addition() – returns the addition of Value1 and Value2. 
# •	Subtraction() – returns the subtraction of Value1 and Value2. 
# •	Multiplication() – returns the multiplication of Value1 and Value2. 
# •	Division() – returns the division of Value1 and Value2 (handle division by zero properly). 
# •	Create multiple objects of the Arithmetic class and invoke all the instance methods. 

from Assignment26_Module import DisplayModule

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the Value1 : "))
        self.Value2 = int(input("Enter the Value2 : "))

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Subtraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2
    
DisplayModule()

Obj = Arithmetic()

Obj.Accept()

print(f"Addition of {Obj.Value1} and {Obj.Value2} is : {Obj.Addition()}")
print(f"Subtraction of {Obj.Value1} and {Obj.Value2} is : {Obj.Subtraction()}")
print(f"Multiplication of {Obj.Value1} and {Obj.Value2} is : {Obj.Multiplication()}")
print(f"Division of {Obj.Value1} and {Obj.Value2} is : {Obj.Division()}")
