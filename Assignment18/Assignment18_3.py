# Write a program which accept N numbers from user and store it into List.Return Minimum number from that list.
# Input: Number of elements : 7
# Input Elements : 13   5   45  7   4   56  34
# Output : 56

from Assignment18_Module import DisplayModule

def MinimumNumberFromList(Data):
    return min(Data)

def MinimumNumberFromListUsingLoop(Data):
    MinNumber = Data[0]
    for no in Data:
        if no < MinNumber:
            MinNumber = no

    return MinNumber

def main():
    DisplayModule()

    print("\n")

    Arr = list()

    Number = int(input("Enter number of elements : "))
    
    for i in range(Number):
        No = int(input("Enter input elements : "))
        
        Arr.append(No)
    
    Ret = MinimumNumberFromList(Arr)
    
    print(f"Minimum number from that list : {Ret}")

    print("\n")
    
    Ret1 = MinimumNumberFromListUsingLoop(Arr)

    print(f"Minimum number using loop from that list  : {Ret1}")

if __name__ == "__main__":
    main()    