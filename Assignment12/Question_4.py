# Write a program which accept one number and prints that many numbers starting from 1
# Input: 5
# Output: 1 2 3 4 5
from Assignment12_Module import PrintNumbersModule

def PrintNumbers(Number):
    StrNumbers = ""
    for i in range(1, Number+1):
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
    Ret = PrintNumbers(Number)
    print(Ret)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the number : "))
    Ret1 = PrintNumbersModule(Number1)
    print(Ret1)

if __name__ == "__main__":
    main()