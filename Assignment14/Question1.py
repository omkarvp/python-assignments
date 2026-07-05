# Write a lambda function which accept one number and return square of that number
  
from Assignment14_Module import DisplayModule,lambdaSquareModule

Square = lambda Num : Num * Num

def main():

    DisplayModule()

    Number = int(input("Enter the number : "))
    
    Ret = Square(Number)

    print(f"Squre of {Number} is : {Ret}")

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Number = int(input("Enter the number : "))
    
    Ret = lambdaSquareModule(Number)

    print(f"Squre of {Number} is : {Ret}")

if __name__ == "__main__":
    main()