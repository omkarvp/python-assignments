# Write a program which contains one function named as Display() that prints "Jay Ganesh" on console
# Two ways to write 
# 1 - By calling function Display() and directly print the statement
# 2 - By accepting input from user and passing that input as an argument to the function DisplayAcceptedInput(inputStr) in 
# function call and using that paramenter in function defination def DisplayAcceptedInput(value): where parameter "value" 
# holds "inputStr"
from Assignment9_Module import DisplayAcceptedInputModule,DisplayModule

def DisplayAcceptedInput(value):
    print(value)

def Display():
    print("Jay Ganesh")

def main():
    print("*"*15)
    Display()
    print("*"*15)
    inputStr = input("Enter the input : ")
    DisplayAcceptedInput(inputStr)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    print("*"*15)
    DisplayModule()
    print("*"*15)
    inputStr = input("Enter the input : ")
    DisplayAcceptedInputModule(inputStr)


if __name__ == "__main__":
    main()