# Write program which accepts one number and checks whether it is perfect number or not
# Input: 6
# Output: Perfect Number
from Assignmen_13Module import isPerfectNumberModule

def isPerfectNumber(Num):
    if Num <= 1:
        return False
    
    Sum = 1
    SquareRoot = int(pow(Num, 0.5))
    for i in range(2,SquareRoot+1):
        if Num % i == 0:
            Sum += i
            if i != Num // i:
                Sum += Num // i
                
    return Sum == Num

def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    Number = int(input("Enter the Number : "))
    Ret = isPerfectNumber(Number)
    if Ret:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the Number : "))
    Ret1 = isPerfectNumberModule(Number1)
    if Ret1:
        print("Perfect Number")
    else:
        print("Not Perfect Number")

if __name__ == "__main__":
    main()