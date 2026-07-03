# Write a program which accepts one number and prints its factor
# Input: 12
# Output: 1 2 3 4 6 12
from Assignment12_Module import FactorModule

def Factor(No):
    Factor = ""
    for i in range(1,No+1):
        if No % i == 0:
            Factor += str(i) + " "

    return Factor


def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    print("*"*21)
    print("=====Print Factor====")
    print("*"*21)

    Number = int(input("Enter the number : "))
    Ret = Factor(Number)
    print("Factor of",Number,":",Ret)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Number1 = int(input("Enter the number : "))
    Ret1 = FactorModule(Number1)
    print("Factor of",Number,":",Ret1)


if __name__ == "__main__":
    main()