# Write a program which accepts one number and print sum of first N Natural numbers
# Input: 5
# Output: 15
from Assignment10_Module import SumOfNaturalNumberModule


def SumOfNaturalNumber(value):
    SumOfNaturalNumbers = 0
    
    for i in range(1,value+1):
        if type(i) == int and i > 0:
            SumOfNaturalNumbers += i    

    print(SumOfNaturalNumbers)

def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*34)
    Display()
    print("*"*34)
    print("=====Sum of N Natural Numbers=====")
    print("*"*34)
    Number = int(input("Enter the number : "))
    SumOfNaturalNumber(Number)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the number : "))
    SumOfNaturalNumberModule(Number1)


if __name__ == "__main__":
    main()