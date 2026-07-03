# Write a program which accepts one number and prints the square of that number
# Input: 5
# Output: 25
from Assignment9_Module import DisplayModule,lambdaDisplaySquareModule,DisplaySquareModule

lambdaDisplaySquare = lambda value:value * value
    
def DisplaySquare(value):
    Square = value * value
    print("Square of ",value," is : ",Square)

def main():
    print("*"*21)
    DisplayModule()
    print("*"*21)

    print("*"*15)
    print("First way is by calling function only ")
    print("*"*15)

    Number1 = int(input("Enter the nuber : "))   
    DisplaySquare(Number1)

    print("*"*15)
    print("Second way is using lambda function ")
    print("*"*15)

    Num1 = int(input("Enter the nuber : "))
    Ret = lambdaDisplaySquare(Num1)
    print("Square of ",Num1," is : ",Ret)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number2 = int(input("Enter the nuber : "))   
    DisplaySquareModule(Number2)

    print("*"*33)
    print("=====Using lambda Module ====")
    print("*"*33)

    Num2 = int(input("Enter the nuber : "))
    Ret2 = lambdaDisplaySquareModule(Num2)
    print("Square of ",Num2," is : ",Ret2)
    
if __name__ == "__main__":
    main()