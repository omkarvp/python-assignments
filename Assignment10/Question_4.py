# Write a program which accepts one number and print all the even number till that number
# Input: 10
# Output: 2 4 6 8 10
from Assignment10_Module import DisplayAllEvenNumberModule

def DisplayAllEvenNumber(value):
    AllEvenNumbers = ""
    for i in range(1,value+1):
        if i % 2 == 0:
            AllEvenNumbers += str(i) + " "
    if value > 1:
        print("All Even numbers till the",value,"are :",AllEvenNumbers)
    else:
        print("Number should be greater than 1")

def Display():
    print("*"*12,"Jay Ganesh","*"*11)

def main():
    print("*"*35)
    Display()
    print("*"*35)
    print("=====All Even Numbers till N Number====")
    print("*"*35)
    Number = int(input("Enter the number : "))
    DisplayAllEvenNumber(Number)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the number : "))
    DisplayAllEvenNumberModule(Number1)

if __name__ == "__main__":
    main()