# Write a program which accepts one number and print sum of digits
# Input: 123
# Output: 6
from Assignment11_Module import SumOfDigitUsingIntTypeModule,SumOfDigitUsingStrTypeModule

def SumOfDigitUsingIntType(Number):
    Sum = 0
    Digit = str(Number)
    for i in range(len(Digit)):
        Sum += int(Digit[i])

    return Sum

def SumOfDigitUsingStrType(Number):
    Sum = 0
    for i in range(len(Number)):
        Sum += int(Number[i])

    return Sum
    
def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)
    print("*"*21)
    print("=====Count Digit Using str Type ====")
    print("*"*21)

    StrNumber = input("Enter the number : ")

    StrRet = SumOfDigitUsingStrType(StrNumber)
    print("Using str Data type Sum of digits : ",StrRet)

    print("*"*21)
    print("=====Count Digit Using int Type ====")
    print("*"*21)

    IntNumber = int(input("Enter the number : "))

    IntRet = SumOfDigitUsingIntType(IntNumber)
    print("Using int Data type Sum of digits : ",IntRet)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    StrNumber1 = input("Enter the number : ")

    StrRet1 = SumOfDigitUsingStrTypeModule(StrNumber1)
    print("Using str Data type Sum of digits : ",StrRet1)

    print("*"*21)
    print("=====Count Digit Using int Type ====")
    print("*"*21)

    IntNumber1 = int(input("Enter the number : "))

    IntRet1 = SumOfDigitUsingIntTypeModule(IntNumber1)
    print("Using int Data type Sum of digits : ",IntRet1)

if __name__ == "__main__":
    main()