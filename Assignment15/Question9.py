# Write a lambda function using reduce() which accepts list of numbers and returns the Product of all elements
from functools import reduce
from Assignment15_Module import DisplayModule,lambdaProductOfAllElementsModule

ProductOfAllElements = lambda Num1, Num2 : Num1 * Num2

def main():

    DisplayModule()

    Arr = list()

    Element = int(input("Enter the number of elements : "))

    for i in range(Element):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = reduce(ProductOfAllElements,Arr)

    print(f"The Product of all elements is : {Ret}")

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Arr = list()

    Element = int(input("Enter the number of elements : "))

    for i in range(Element):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = reduce(lambdaProductOfAllElementsModule,Arr)

    print(f"The Product of all elements is : {Ret}")

if __name__ == "__main__":
    main()