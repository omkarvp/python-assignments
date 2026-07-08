# Write a program which accept one number from user and return addition of it's factor
# Input: 5
# Output: 16

from Assignment17_Module import DisplayModule

def AdditionOfFactors(value):
    AdditionOfFactor = 0

    for i in range(1,value):
        if value % i == 0:
            AdditionOfFactor = AdditionOfFactor + i
        
    return AdditionOfFactor

def main():
    print("*"*35)
    DisplayModule()
    print("*"*35)
    
    print("")
    print("")

    print("=====Addition of Factors====")
    print("*"*35)
    Number = int(input("Enter the number : "))
    Ret = AdditionOfFactors(Number)
    print(f"Addition of factors is : {Ret}")

if __name__ == "__main__":
    main()