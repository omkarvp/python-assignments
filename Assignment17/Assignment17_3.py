# Write a program which accept one number from user and return it's factorial
# Input: 5
# Output: 120

from Assignment17_Module import DisplayModule

def DisplayFactorialNumber(value):
    FactorialNumbers = 1

    for i in range(1,value+1):
        FactorialNumbers = FactorialNumbers*i
    
    return FactorialNumbers

def main():
    print("*"*35)
    DisplayModule()
    print("*"*35)
    
    print("")
    print("")

    print("=====Factorial Numbers====")
    print("*"*35)
    Number = int(input("Enter the number : "))
    Ret = DisplayFactorialNumber(Number)
    print(f"Factorial Number of {Number} is : {Ret}")

if __name__ == "__main__":
    main()