# Write a lambda function which accept two numbers and returns Multiplication

from Assignment14_Module import DisplayModule,lambdaMultiplication

Multiplication = lambda Num1, Num2 : Num1 * Num2

def main():

    DisplayModule()

    Number1 = int(input("Enter the first number : "))
    
    Number2 = int(input("Enter the second number : "))
    
    Ret = Multiplication(Number1,Number2)

    print(f"Multiplication of {Number1} and {Number2} is : {Ret}")

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the first number : "))
    
    Number2 = int(input("Enter the second number : "))
    
    Ret = lambdaMultiplication(Number1,Number2)

    print(f"Multiplication of {Number1} and {Number2} is : {Ret}")

if __name__ == "__main__":
    main()