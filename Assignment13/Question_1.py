# Write a Program which accepts length and width of rectangle and prints area
from Assignmen_13Module import LambdaAreaModule,AreaModule

LambdaArea = lambda Length,Width : Length * Width

def Area(Length, Width):
    Area = Length * Width
    return Area

def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    Length = int(input("Enter the length : "))
    Width = int(input("Enter the width : "))
    CalculateArea = Area(Length,Width)
    print("Area : ",CalculateArea)

    print("*"*21)
    print("*"*5,"Using lambda","*"*6)
    print("*"*21)

    Length1 = int(input("Enter the length : "))
    Width1 = int(input("Enter the width : "))
    LambdaCalculateArea = LambdaArea(Length1,Width1)
    print("Using Lambda Area : ",LambdaCalculateArea)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Length2 = int(input("Enter the length : "))
    Width2 = int(input("Enter the width : "))
    CalculateAreaModule = AreaModule(Length2,Width2)
    print("Using Module Function Area : ",CalculateAreaModule)

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Length3 = int(input("Enter the length : "))
    Width3 = int(input("Enter the width : "))
    LambdaCalculateAreaModule = LambdaAreaModule(Length3,Width3)
    print("Using Module Lambda Area : ",LambdaCalculateAreaModule)

if __name__ == "__main__":
    main()