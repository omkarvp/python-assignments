# Write a program which accept one number and display below pattern
# input: 5
#       0   1   2   3   4
#   0   1
#   1   1   2
#   2   1   2   3
#   3   1   2   3   4
#   4   1   2   3   4   5

from Assignment17_Module import DisplayModule

def PrintPattern(Number):
    PatternStr = ""

    for i in range(1,Number+1):
        for j in range(1,i+1):
            PatternStr += str(j) + "  "
        PatternStr+= "\n"

    print(PatternStr)

def main():
    DisplayModule()

    Number  = int(input("Enter the number : "))
    PrintPattern(Number)


if __name__ == "__main__":
    main()

