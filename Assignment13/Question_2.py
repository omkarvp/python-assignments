# Write a Program which accepts radius of circle and prints area of circle.
from Assignmen_13Module import AreaOfCircleModule,LambdaAreaOfCircleModule

pi = 3.14 # for lambda function set global variable
LambdaAreaOfCircle = lambda radius : pi * radius * radius

def AreaOfCircle(radius):
    pi = 3.14 
    Area = pi * radius * radius
    return Area

def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    Radius = int(input("Enter the radius : "))
    CalculateArea = AreaOfCircle(Radius)
    print("Area of Circle : ",CalculateArea)

    print("*"*21)
    print("*"*5,"Using lambda","*"*6)
    print("*"*21)

    Radius1 = int(input("Enter the radius : "))
    LambdaCalculateAreaOfCircle = LambdaAreaOfCircle(Radius1)
    print("Using Lambda Area of Circle : ",LambdaCalculateAreaOfCircle)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Radius2 = int(input("Enter the radius : "))
    CalculateAreaModule = AreaOfCircleModule(Radius2)
    print("Area of Circle : ",CalculateAreaModule)

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Radius3 = int(input("Enter the radius : "))
    LambdaCalculateAreaOfCircleModule = LambdaAreaOfCircleModule(Radius3)
    print("Using Lambda Area of Circle : ",LambdaCalculateAreaOfCircleModule)

if __name__ == "__main__":
    main()

