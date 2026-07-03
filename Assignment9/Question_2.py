# Write a program which contains one function ChkGreater() that accepts two numbers and prints the greater number
# Input: 10 20
# Output: 20 is greater
from Assignment9_Module import DisplayModule,listInputChkGreaterModule,ChkGreaterModule

def listInputChkGreater(Data):
    GreateNumber = 0
    for no in Data:
        if(no > GreateNumber):
            GreateNumber = no
        
    print(GreateNumber, "is greater")

def ChkGreater(No1,No2):
    if (No1 > No2):
        print(No1, "is greater")
    else:
        print(No2, "is greater")

def main():
    Number1 = int(input("Enter first number : "))
    Number2 = int(input("Enter second number : "))
    ChkGreater(Number1,Number2)

    print("*"*15)
    print("Second way to accepts two numbers and stored it into list and pass that ")
    print("list as function argument while calling function to the function defination")
    print("*"*15)

    listData = list()
    Num1 = int(input("Enter first number : "))
    listData.append(Num1)
    Num2 = int(input("Enter second number : "))
    listData.append(Num2)
    listInputChkGreater(listData)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number3 = int(input("Enter first number : "))
    Number4 = int(input("Enter second number : "))
    ChkGreaterModule(Number3,Number4)

    print("*"*15)
    print("Second way to accepts two numbers and stored it into list and pass that ")
    print("list as function argument while calling function to the function defination")
    print("*"*15)

    listData1 = list()
    Num3 = int(input("Enter first number : "))
    listData1.append(Num3)
    Num4 = int(input("Enter second number : "))
    listData1.append(Num4)
    listInputChkGreaterModule(listData1)
    

if __name__ == "__main__":
    main()