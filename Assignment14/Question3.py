# Write a lambda function which accept two numbers and return maximum number

from Assignment14_Module import DisplayModule,lambdaMaximumNumber

MaximumNumber = lambda Num1, Num2 : Num1 > Num2

def main():

    DisplayModule()

    Number1 = int(input("Enter the first number : "))
    
    Number2 = int(input("Enter the second number : "))
    
    Ret = MaximumNumber(Number1,Number2)

    if Ret == True:
        print(f"Maximum Number is : {Number1}")
    else:
        print(f"Maximum Number is : {Number2}")


    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the first number : "))
    
    Number2 = int(input("Enter the second number : "))
    
    Ret = lambdaMaximumNumber(Number1,Number2)

    if Ret == True:
        print(f"Maximum Number is : {Number1}")
    else:
        print(f"Maximum Number is : {Number2}")

if __name__ == "__main__":
    main()