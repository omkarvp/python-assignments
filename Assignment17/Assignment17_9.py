# Write a program which accept number from user and return number of digits in that number
# Input: 5187934
# Output: 7

from Assignment17_Module import DisplayModule

def NumberOfDigits(Number):
    LengthOfNumberToStr = len(str(Number))

    return LengthOfNumberToStr

def main():
    DisplayModule()

    Number  = int(input("Enter the number : "))
    
    Ret = NumberOfDigits(Number)

    print(f"Number of digits in {Number} is : {Ret}")


if __name__ == "__main__":
    main()

