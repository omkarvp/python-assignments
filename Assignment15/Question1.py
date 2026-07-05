# Write a lambda function using map() which accepts list of numbers and returns list of squares of each number
from Assignment15_Module import DisplayModule,lambdaSquareModule

Square = lambda No1 : No1 * No1

def main():
    DisplayModule()

    Arr = list()

    Element = int(input("Enter the number of elements : "))

    for i in range(Element):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = list(map(Square,Arr))

    print(f"List of Square numbers is : ",Ret)

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Arr = list()

    Element = int(input("Enter the number of elements : "))

    for i in range(Element):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = list(map(lambdaSquareModule,Arr))
    
    print(f"List of Square numbers is : ",Ret)

if __name__ == "__main__":
    main()