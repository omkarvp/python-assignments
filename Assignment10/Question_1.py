# Write a program which accepts one number and prints multiplication table of that number
# Input: 4
# Output: 4 8 12 16 20 24 28 32 36 40
from Assignment10_Module import MultiplicationTableModule

def MultiplicationTable(value):
    table = ""
    mult = 0
    for i in range(1,11):
        mult = i * value
        table = table + str(mult) + " "

    print(table)

def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    print("*"*30)
    print("=====Multiplication Table=====")
    print("*"*30)
    Number = int(input("Enter the Number : "))
    MultiplicationTable(Number)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the Number : "))
    MultiplicationTableModule(Number1)

if __name__ == "__main__":
    main()