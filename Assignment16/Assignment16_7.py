# Write a program which contains one function that accept one number from user 
# and return True if number is divisible by otherwise return False

from Assignment16_Module import DisplayModule 

def DivisibleByFive(No):
    if No % 5 == 0:
        return True
    else:
        return False

def main():
    DisplayModule()

    Number = int(input("Enter the number : "))
    
    Ret = DivisibleByFive(Number)

    print(f"Divisible by 5 : {Ret}")


if __name__ == "__main__":
    main()