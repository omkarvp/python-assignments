# Write a lambda function using filter() which accepts list of numbers and returns list of Odd numbers
from Assignment15_Module import DisplayModule,lambdaOddNumberModule

OddNumber = lambda Num : Num % 2 != 0

def main():

    DisplayModule()

    Arr = list()

    Element = int(input("Enter the number of elements : "))

    for i in range(Element):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = list(filter(OddNumber,Arr))

    print(f"List of Odd numbers is : ",Ret)

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Arr = list()

    Element = int(input("Enter the number of elements : "))

    for i in range(Element):
        No = int(input("Enter number : "))
        Arr.append(No)

    Ret = list(filter(lambdaOddNumberModule,Arr))
    
    print(f"List of Odd numbers is : ",Ret)

if __name__ == "__main__":
    main()