# Write a program which accept name from user and display it's length of it's name

from Assignment16_Module import DisplayModule 

def LengthOfName(Value): 
    print(f"Length of name {Value} is : {len(Value)}")

def main():
    DisplayModule()
    Name = input("Enter the name : ")
    LengthOfName(Name)

if __name__ == "__main__":
    main()