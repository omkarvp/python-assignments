# Write a program which accept one number and display below pattern
# input: 5
#    0   1   2   3   4
#0   *   *   *   *   *
#1   *   *   *   *
#2   *   *   *
#3   *   *
#4   *

from Assignment17_Module import DisplayModule

def PrintPattern(Number):
    PatternStr = ""
    
    Counter = 1

    for i in range(Number):
        for j in range(Number-i):
            PatternStr += "*  "
        PatternStr+= "\n"

    print(PatternStr)

def main():
    DisplayModule()

    Number  = int(input("Enter the number : "))
    PrintPattern(Number)


if __name__ == "__main__":
    main()

