# Write a program which accepts two numbers and prints its addition,substraction,multiplication and division
from Assignment12_Module import CalculationsModule
def Calculations(No1, No2):
    Addition = No1 + No2
    Substraction = No1 - No2
    Multiplication = No1 * No2
    Division = No1 / No2

    return Addition,Substraction,Multiplication,Division

def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    print("*"*21)
    print("=====Arithmatic Operations====")
    print("*"*21)

    Number1 = int(input("Enter first number : "))
    Number2 = int(input("Enter second number : "))
    Addition,Substraction,Multiplication,Division = Calculations(Number1,Number2)

    print("Addition is : ",Addition)
    print("Substraction is : ",Substraction)
    print("Multiplication is : ",Multiplication)
    print("Division is : ",Division)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number3 = int(input("Enter first number : "))
    Number4 = int(input("Enter second number : "))
    Addition1,Substraction1,Multiplication1,Division1 = CalculationsModule(Number3,Number4)

    print("Addition is : ",Addition1)
    print("Substraction is : ",Substraction1)
    print("Multiplication is : ",Multiplication1)
    print("Division is : ",Division1)

if __name__ == "__main__":
    main()