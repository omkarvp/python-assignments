# Write a program which accepts one number and prints the cube of that number
# Input: 3
# Output: 27
from Assignment9_Module import DisplayModule,lambdaDisplayCubeModule,DisplayCubeModule


lambdaDisplayCube = lambda value:value * value * value
    
def DisplayCube(value):
    Cube = value * value * value
    print("Cube of ",value," is : ",Cube)

def main():
    print("*"*21)
    DisplayModule()
    print("*"*21)


    print("*"*15)
    print("First way is by calling function only ")
    print("*"*15)

    Number1 = int(input("Enter the number : "))
    DisplayCube(Number1)

    print("*"*15)
    print("Second way is using lambda function ")
    print("*"*15)

    Num1 = int(input("Enter the number : "))
    Ret = lambdaDisplayCube(Num1)
    print("Cube of ",Num1," is : ",Ret)


    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number2 = int(input("Enter the number : "))
    DisplayCubeModule(Number2)

    print("*"*33)
    print("=====Using lambda Module ====")
    print("*"*33)

    Num2 = int(input("Enter the number : "))
    Ret2 = lambdaDisplayCubeModule(Num2)
    print("Cube of ",Num2," is : ",Ret2)

    
if __name__ == "__main__":
    main()