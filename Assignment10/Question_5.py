# Write a program which accepts one number and print all the odd number till that number
# Input: 10
# Output: 1 3 5 7 9
from Assignment10_Module import DisplayAllOddNumberModule

def DisplayAllOddNumber(value):
    AllOddNumbers = ""
    for i in range(1,value+1):
        if i % 2 != 0:
            AllOddNumbers += str(i) + " "
    if value > 1:
        print("All Odd numbers till the",value,"are :",AllOddNumbers)
    else:
        print("Number should be greater than 1")

def Display():
    print("="*13,"Jay Ganesh","="*13)

def main():
    print("*"*38)
    Display()
    print("*"*38)
    print("=====All Odd Numbers till N Number====")
    print("*"*38)
    Number = int(input("Enter the number : "))
    DisplayAllOddNumber(Number)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the number : "))
    DisplayAllOddNumberModule(Number1)

if __name__ == "__main__":
    main()