# Write a lambda function which accept one numbers and return True if divisible by 5

from Assignment14_Module import DisplayModule,lambdaDivisibleByFive

DivisibleByFive = lambda Num : Num % 5 == 0

def main():

    DisplayModule()

    Number = int(input("Enter the number : "))
    
    Ret = DivisibleByFive(Number)

    print(Ret)


    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Number = int(input("Enter the number : "))
    
    Ret = lambdaDivisibleByFive(Number)

    print(Ret)

if __name__ == "__main__":
    main()