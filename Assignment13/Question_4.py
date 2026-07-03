# Write program to accept one number and print binary equivalent
from Assignmen_13Module import DecimalToBinaryModule

def DecimalToBinary(num):
    if num == 0:
        return "0"
        
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    return binary


def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    Number = int(input("Enter the Number : "))
    Ret = DecimalToBinary(Number)
    print("Binary Equivalent ",Ret)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the Number : "))
    Ret1 = DecimalToBinaryModule(Number1)
    print("Binary Equivalent ",Ret1)

if __name__ == "__main__":
    main()