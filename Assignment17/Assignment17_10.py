# Write a program which accept number from user and return addition of digits in that number
# Input: 5187934
# Output: 37

from Assignment17_Module import DisplayModule

def AdditionOfNumberOfDigits(Number):
    Sum = 0
    NumberToStr = str(Number)
    Length = len(NumberToStr)
    for i in range(Length):
        Sum += int(NumberToStr[i])

    return Sum

def main():
    DisplayModule()

    Number  = int(input("Enter the number : "))
    
    Ret = AdditionOfNumberOfDigits(Number)

    print(f"Addition of digits in the Number {Number} is : {Ret}")


if __name__ == "__main__":
    main()

