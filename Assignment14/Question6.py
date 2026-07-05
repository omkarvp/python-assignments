# Write a lambda function which accept one numbers and return True if number is Odd otherwise False

from Assignment14_Module import DisplayModule,lambdaOddNumber

OddNumber = lambda Num : Num % 2 != 0

def main():

    DisplayModule()

    Number = int(input("Enter the number : "))
    
    Ret = OddNumber(Number)

    if Ret == True:
        print(f"Number {Number} is Odd")


    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Number = int(input("Enter the number : "))
    
    Ret = lambdaOddNumber(Number)

    if Ret == True:
        print(f"Number {Number} is Odd")

if __name__ == "__main__":
    main()