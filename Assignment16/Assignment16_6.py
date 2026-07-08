# Write a program which accept number from user and check whether that number is positive or negative  or zero

from Assignment16_Module import DisplayModule 

def CheckNumber(No):
    if No == 0:
        print("Zero")
    elif No < 0:
        print("Negative Number")
    else:
        print("Positive Number")

def main():
    DisplayModule()

    Number = int(input("Enter the number : "))
    CheckNumber(Number)

if __name__ == "__main__":
    main()