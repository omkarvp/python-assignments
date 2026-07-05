# Write a lambda function which accept one number and return Cube of that number

from Assignment14_Module import DisplayModule,lambdaCubeModule

Cube = lambda Num : Num * Num * Num

def main():

    DisplayModule()

    Number = int(input("Enter the number : "))
    
    Ret = Cube(Number)

    print(f"Cube of {Number} is : {Ret}")

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Number = int(input("Enter the number : "))
    
    Ret = lambdaCubeModule(Number)

    print(f"Cube of {Number} is : {Ret}")

if __name__ == "__main__":
    main()