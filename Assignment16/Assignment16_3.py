# Write a program which contains one function named as Add() which accepts two numbers from user 
# and return addition of that two numbers. 

from Assignment16_Module import DisplayModule 

def Add(No1, No2):
    return No1 + No2


def main():
    DisplayModule()

    Number1 = int(input("Enter first number : "))
    
    Number2 = int(input("Enter second number : "))
    
    Ret = Add(Number1, Number2)

    print(f"Addition of {Number1} and {Number2} is : {Ret}")

if __name__ == "__main__":
    main()