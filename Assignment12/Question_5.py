# Write a program which accept one number and prints that many numbers in reverse order
# Input: 5
# Output: 1 2 3 4 5
from Assignment12_Module import PrintReverseNumbersModule

def PrintReverseNumbers(Number):
    StrNumbers = ""
    for i in range(Number,0,-1):
        StrNumbers += str(i) + " "

    return StrNumbers

def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    print("*"*21)
    print("=====Print Numbers starting from 1=====")
    print("*"*21)

    Number = int(input("Enter the number : "))
    Ret = PrintReverseNumbers(Number)
    print(Ret)

    print("*"*21)
    print("*"*5,"Using Function Module","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the number : "))
    Ret1 = PrintReverseNumbersModule(Number1)
    print(Ret1)


if __name__ == "__main__":
    main()