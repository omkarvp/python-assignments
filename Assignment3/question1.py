def Calculation(No1, No2):
    Multiplication  = No1 * No2
    return Multiplication

def main():
    Value1      = int(input("Enter first number : "))
    Value2      = int(input("Enter second number : "))
    Ret1        = Calculation(Value1, Value2)
    print("Multiplication is : ",Ret1)

if __name__ == "__main__":
    main()