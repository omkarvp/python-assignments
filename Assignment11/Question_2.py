# Write a program which accepts one number and print count of digits in that number
# Input: 7521
# Output: 4
from Assignment11_Module import lambdaCountDigitModule,CountDigitModule

lambdaCountDigit = lambda Number :len(str(Number))

def CountDigit(Number):
    Count = len(str(Number))
    return Count
    
def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)
    print("*"*21)
    print("=====Count Digit====")
    print("*"*21)

    Number = int(input("Enter the number : "))

    Ret = CountDigit(Number)
    print("Total number of digits : ",Ret)

    print("*"*33)
    print("=====Using lambda Count Digit====")
    print("*"*33)

    Number1 = int(input("Enter the number : "))

    Ret1 = lambdaCountDigit(Number1)
    print("Using lambda Total number of digits : ",Ret1)


    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number2 = int(input("Enter the number : "))

    Ret2 = CountDigitModule(Number2)
    print("Total number of digits : ",Ret2)

    print("*"*33)
    print("=====Using lambda Module Count Digit====")
    print("*"*33)

    Number3 = int(input("Enter the number : "))

    Ret3 = lambdaCountDigitModule(Number3)
    print("Using lambda Total number of digits : ",Ret3)

if __name__ == "__main__":
    main()