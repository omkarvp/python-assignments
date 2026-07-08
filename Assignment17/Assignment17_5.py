# Write a program which accept one number from user and check whether number is Prime or not
# Input: 5
# Output: It is Prime Number

from Assignment17_Module import DisplayModule

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

def main():
    print("*"*21)
    DisplayModule()
    print("*"*21)

    print("*"*21)
    print("=====Prime Number====")
    print("*"*21)

    Number = int(input("Enter the number : "))

    Ret = isPrimeNumber(Number)
    print(Ret)
    if Ret:
        print("It is Prime Number")
    else:
        print("It is not Prime Number")

if __name__ == "__main__":
    main()