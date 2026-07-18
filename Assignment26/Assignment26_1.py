# 1: Write a Python program to implement a class named Demo with the following specifications:
# •	The class should contain two instance variables: no1 and no2. 
# •	The class should contain one class variable named Value. 
# •	Define a constructor (__init__) that accepts two parameters and initializes the instance variables. 
# •	Implement two instance methods: 
# o	Fun() – displays the values of instance variables no1 and no2. 
# o	Gun() – displays the values of instance variables no1 and no2. 
# Create two objects of the Demo class as follows:
# Obj1 = Demo(11, 21)

# Obj2 = Demo(51, 101)
# Call the instance methods in the given sequence:
# Obj1.Fun()

# Obj2.Fun()

# Obj1.Gun()

# Obj2.Gun()

from Assignment26_Module import DisplayModule

class Demo:
    Value = 31

    def __init__(self,Number1,Number2):
        self.no1 = Number1
        self.no2 = Number2
    
    def Fun(self):
        print(f"From Fun() The value of instance variable are no1 : {self.no1} and no2 : {self.no2}")

    def Gun(self):
        print(f"From Gun() The value of instance variable are no1 : {self.no1} and no2 : {self.no2}")
    
Obj1 = Demo(11, 21)

Obj2 = Demo(51, 101)

DisplayModule()

Obj1.Fun()

Obj2.Fun()

Obj1.Gun()

Obj2.Gun()