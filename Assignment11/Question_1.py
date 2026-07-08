# Write a program which accepts one number and checks whether it is prime number or not
# Input: 11
# Output: Prime Number
from Assignment11_Module import isPrimeNumberModule

def isPrimeNumber(Number):
    if Number <= 1:
        return False
    
    if Number == 2:
        return True
    
    if Number % 2 == 0:
        return False
    
    # Check divisibility from 2 to n-1
    for i in range(2, Number):
        if Number % i == 0:
            return False
     
    return True
    
def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    print("*"*21)
    print("=====Prime Number====")
    print("*"*21)

    Number = int(input("Enter the number : "))

    Ret = isPrimeNumber(Number)

    if Ret:
        print("Prime Number")
    else:
        print("Not Prime Number")

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the number : "))

    Ret1 = isPrimeNumberModule(Number1)

    if Ret1:
        print("Prime Number")
    else:
        print("Not Prime Number")


if __name__ == "__main__":
    main()