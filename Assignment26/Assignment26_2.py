# 2: Write a Python program to implement a class named Circle with the following requirements:
# •	The class should contain three instance variables: Radius, Area, and Circumference. 
# •	The class should contain one class variable named PI, initialized to 3.14. 
# •	Define a constructor (__init__) that initializes all instance variables to 0.0. 
# •	Implement the following instance methods: 
# o	Accept() – accepts the radius of the circle from the user. 
# o	CalculateArea() – calculates the area of the circle and stores it in the Area variable. 
# o	CalculateCircumference() – calculates the circumference of the circle and stores it in the Circumference variable. 
# o	Display() – displays the values of Radius, Area, and Circumference. 
# •	Create multiple objects of the Circle class and invoke all the instance methods for each object. 

from Assignment26_Module import DisplayModule

class Circle:

    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the Radius of the Circle : "))

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius ** 2

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):

        print(f"The Radius of the Circle is : {self.Radius}")
        print(f"The Area of the Circle is : {self.Area}")
        print(f"The Circumference of the Circle is : {self.Circumference}")


DisplayModule()

Obj = Circle()

Obj.Accept()
Obj.CalculateArea()
Obj.CalculateCircumference()
Obj.Display()


