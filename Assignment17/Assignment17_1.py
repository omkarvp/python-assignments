# Create on module name as Arithmatic which contains 4 functions as 
# Add() for Addition, 
# Sub() for Substraction,
# Mult() for Multiplication,
# Div() for Division,
# All functions accepts two parameters as number and perform the operation.
# Write on python program which call all the functions from Arithmatic module by Accepting parameters from user.

from Assignment17_Module import DisplayModule
from Arithmatic import Add,Sub,Mult,Div

def main():
    DisplayModule()

    print("*"*21)
    print("====Addition of 2 Number====")
    print("*"*21)
    Number1 = int(input("Enter the first number : "))
    Number2 = int(input("Enter the second number : "))
    
    Addition = Add(Number1,Number2)
    
    print(f"Addition of {Number1} and {Number2} is : {Addition}")

    print("")
    print("")
    print("*"*21)
    print("====Substraction of 2 Number====")
    print("*"*21)
    Number1 = int(input("Enter the first number : "))
    Number2 = int(input("Enter the second number : "))
    
    Substraction = Sub(Number1,Number2)
    
    print(f"Substraction of {Number1} and {Number2} is : {Substraction}")

    print("")
    print("")
    print("*"*21)
    print("====Multiplication of 2 Number====")
    print("*"*21)
    Number1 = int(input("Enter the first number : "))
    Number2 = int(input("Enter the second number : "))
    
    Multiplication = Mult(Number1,Number2)
    
    print(f"Multiplication of {Number1} and {Number2} is : {Multiplication}")

    print("")
    print("")
    print("*"*21)
    print("====Division of 2 Number====")
    print("*"*21)
    Number1 = int(input("Enter the first number : "))
    Number2 = int(input("Enter the second number : "))
    
    Division = Div(Number1,Number2)
    
    print(f"Division of {Number1} and {Number2} is : {Division:.6f}")


if __name__ == "__main__":
    main()

