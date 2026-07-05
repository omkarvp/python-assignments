# Write a lambda function which accept two numbers and returns Addition

from Assignment14_Module import DisplayModule,lambdaAddition

Addition = lambda Num1, Num2 : Num1 + Num2

def main():

    DisplayModule()

    Number1 = int(input("Enter the first number : "))
    
    Number2 = int(input("Enter the second number : "))
    
    Ret = Addition(Number1,Number2)

    print(f"Addition of {Number1} and {Number2} is : {Ret}")

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the first number : "))
    
    Number2 = int(input("Enter the second number : "))
    
    Ret = lambdaAddition(Number1,Number2)

    print(f"Addition of {Number1} and {Number2} is : {Ret}")

if __name__ == "__main__":
    main()