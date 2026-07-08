# Write a program which accept one number and display below pattern
# input: 5
#   *   *   *   *   *
#   *   *   *   *   *
#   *   *   *   *   *
#   *   *   *   *   *
#   *   *   *   *   *

from Assignment17_Module import DisplayModule

def PrintPattern(Number):
    PatternStr = ""

    for i in range(Number):
        for j in range(Number):
            PatternStr += "*  "
        PatternStr+= "\n"

    print(PatternStr)

def main():
    DisplayModule()

    Number  = int(input("Enter the number : "))
    PrintPattern(Number)


if __name__ == "__main__":
    main()

