# Write a lambda function using reduce() which accepts list of numbers and returns the Addition of all elements
from functools import reduce
from Assignment15_Module import DisplayModule,lambdaMinimumNumberModule

MinimumNumber = lambda Num1, Num2 : min(Num1, Num2)

def main():

    DisplayModule()

    Arr = list()

    Element = int(input("Enter the number of elements : "))

    for i in range(Element):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = reduce(MinimumNumber,Arr)

    print(f"Minimum number is : ",Ret)

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Arr = list()

    Element = int(input("Enter the number of elements : "))

    for i in range(Element):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = reduce(lambdaMinimumNumberModule,Arr)

    print(f"Minimum number is : ",Ret)

if __name__ == "__main__":
    main()