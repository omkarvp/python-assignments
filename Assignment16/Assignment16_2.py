# Write a program which contains one function named as ChkNum() which accepts one parameter as number. 
# If number is even then it should display "Even Number"
# otherwise display "Odd Number" on console.

from Assignment16_Module import DisplayModule

def ChkNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


def main():
    DisplayModule()

    ChkNum(11)
    
    ChkNum(8)

if __name__ == "__main__":
    main()