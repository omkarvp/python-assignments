# Write a program which accepts one number and checks whether it is divisible by 3 and 5
# Input: 15
# Output: Divisible by 3 and 5

from Assignment9_Module import DisplayModule,lambdaDivisibleByModule,DivisibleByModule

lambdaDivisibleBy = lambda value:value % 3 == 0 and value % 5 == 0
    
def DivisibleBy(value):
    if value % 3 == 0 and value % 5 == 0:
        print(value, " is divisible by 3 and 5")
    else:
        print(value, " is not divisible only by 3 and 5")

def main():
    print("*"*21)
    DisplayModule()
    print("*"*21)

    print("*"*15)
    print("First way is by calling function only ")
    print("*"*15)

    Number1 = int(input("Enter the number : "))
    
    DivisibleBy(Number1)
    print("*"*15)
    print("Second way is using lambda function ")
    print("*"*15)

    Num1 = int(input("Enter the number : "))
    Ret = lambdaDivisibleBy(Num1)
    if Ret:
        print(Num1, " is divisible by 3 and 5")
    else:
        print(Num1, " is not divisible only by 3 and 5")

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number2 = int(input("Enter the number : "))
    
    DivisibleByModule(Number2)
    print("*"*15)
    print("Second way is using lambda function ")
    print("*"*15)

    print("*"*33)
    print("=====Using lambda Module ====")
    print("*"*33)

    Num2 = int(input("Enter the number : "))
    Ret1 = lambdaDivisibleByModule(Num2)
    if Ret1:
        print(Num2, " is divisible by 3 and 5")
    else:
        print(Num2, " is not divisible only by 3 and 5")

if __name__ == "__main__":
    main()