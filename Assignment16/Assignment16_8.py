# Write a program which accept number from user 
# and print that number of "*" on screen

from Assignment16_Module import DisplayModule 

def printStar(No):
    starStr = ""

    for i in range(No):
        starStr += "* " 
    
    print(starStr)

def main():
    DisplayModule()

    Number = int(input("Enter the number : "))
    
    printStar(Number)

if __name__ == "__main__":
    main()