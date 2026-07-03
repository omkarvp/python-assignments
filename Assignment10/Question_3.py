# Write a program which accepts one number and print sum of first N Natural numbers
# Input: 5
# Output: 120

from Assignment10_Module import DisplayFactorialNumberModule

def DisplayFactorialNumber(value):
    FactorialNumbers = 1
    for i in range(1,value+1):
        FactorialNumbers = FactorialNumbers*i
    
    if value > 0:
        print("Factorial is :",FactorialNumbers)
    else:
        print("Number should be greater than 0")

def Display():
    print("*"*12,"Jay Ganesh","*"*11)

def main():
    print("*"*35)
    Display()
    print("*"*35)
    print("=====Sum of N Factorial Numbers====")
    print("*"*35)
    Number = int(input("Enter the number : "))
    DisplayFactorialNumber(Number)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the number : "))
    DisplayFactorialNumberModule(Number1)

if __name__ == "__main__":
    main()