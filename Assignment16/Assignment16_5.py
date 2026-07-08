# Write a program which display 10 to 1 on screen
# and return addition of that two numbers. 

from Assignment16_Module import DisplayModule 

def Displaynumbers():
    strType = ""
    for i in range(10, 0,-1):
        strType += str(i) + " "
    print(strType)

def main():
    DisplayModule()

    Displaynumbers()

if __name__ == "__main__":
    main()