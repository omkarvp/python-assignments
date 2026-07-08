# Write a program which contains one lambda function which accepts two parameters and return its multiplication.
# Input : 4 3  Output : 12
# Input : 6 3  Output : 18

from Assignment19_Module import DisplayModule

Multipication = lambda No1, No2 : No1 * No2

def main():
    DisplayModule()

    print("\n")
    
    Number1 = int(input("Enter the first number : "))
    Number2 = int(input("Enter the second number : "))
    
    Ret =  Multipication(Number1, Number2)

    print(f"Multiplication of {Number1} and {Number2} is : {Ret}")

if __name__ == "__main__":
    main()