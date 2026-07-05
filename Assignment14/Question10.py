# Write a lambda function which accept three numbers and returns largest number

from Assignment14_Module import DisplayModule,lambdaLargestNumber

LargestNumber = lambda Num1, Num2, Num3 : max(Num1, Num2, Num3)

def main():

    DisplayModule()

    Number1 = int(input("Enter the first number : "))
    
    Number2 = int(input("Enter the second number : "))
    
    Number3 = int(input("Enter the second number : "))

    Ret = LargestNumber(Number1, Number2, Number3)

    print(f"Largest Number is : {Ret}")

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the first number : "))
    
    Number2 = int(input("Enter the second number : "))
    
    Number3 = int(input("Enter the second number : "))

    Ret = lambdaLargestNumber(Number1, Number2, Number3)

    print(f"Largest Number is : {Ret}")

if __name__ == "__main__":
    main()