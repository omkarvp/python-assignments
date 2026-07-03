# Write a program which accepts one number and print reverse of that numbers
# Input: 123
# Output: 321

from Assignment11_Module import ReverseNumberUsingIntTypeModule,ReverseNumberUsingStrTypeModule

def ReverseNumberUsingIntType(Number):
    ReverseString = ""
    Digit = str(Number)
    for i in range(len(Digit)-1, -1,-1):
        ReverseString += Digit[i]

    return ReverseString

def ReverseNumberUsingStrType(Number):
    ReverseString = ""
    for i in range(len(Number)-1, -1,-1):
        ReverseString += Number[i]

    return ReverseString
    
def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)
    print("*"*21)
    print("=====Reverse Digit====")
    print("*"*21)

    Number = input("Enter the number : ")

    Ret = ReverseNumberUsingStrType(Number)
    print("Using str Data type Reverse Number is :",Ret)
    
    print("*"*21)
    print("=====Reverse Digit====")
    print("*"*21)

    Number1 = int(input("Enter the number : "))

    Ret1 = ReverseNumberUsingIntType(Number1)
    print("Using int Data type Reverse Number is :",Ret1)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number2 = input("Enter the number : ")

    Ret2 = ReverseNumberUsingStrTypeModule(Number2)
    print("Using str Data type Reverse Number is :",Ret2)
    
    print("*"*21)
    print("=====Reverse Digit====")
    print("*"*21)

    Number3 = int(input("Enter the number : "))

    Ret3 = ReverseNumberUsingIntTypeModule(Number3)
    print("Using int Data type Reverse Number is :",Ret3)


if __name__ == "__main__":
    main()