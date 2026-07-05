# Write a lambda function using filter() which accepts list of numbers and returns list of numbers divisible by both 3 and 5
from Assignment15_Module import DisplayModule,lambdaDivisibleByModule

DivisibleBy = lambda Num : Num % 3 == 0 and Num % 5 == 0

def main():

    DisplayModule()

    Arr = list()

    Element = int(input("Enter the number of strings : "))

    for i in range(Element):
        Number = int(input("Enter number : "))
        Arr.append(Number)

    Ret = list(filter(DivisibleBy,Arr))

    print(f"List of numbers divisible by both 3 and 5 are : {Ret} ")

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Arr = list()

    Element = int(input("Enter the number of strings : "))

    for i in range(Element):
        Number = int(input("Enter number : "))
        Arr.append(Number)

    Ret = list(filter(lambdaDivisibleByModule,Arr))

    print(f"List of numbers divisible by both 3 and 5 are : {Ret} ")

if __name__ == "__main__":
    main()