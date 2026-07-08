# Write a program which accept N numbers from user and store it into List.Return addition of all elements from that list.
# Input: Number of elements : 6
# Input Elements : 13   5   45  7   4   56
# Output : 130

from Assignment18_Module import DisplayModule

def AdditionOfList(Data):
    Sum = 0
    for no in Data:
        Sum += no

    return Sum

def main():
    DisplayModule()

    print("\n")

    Arr = list()

    Number = int(input("Enter number of elements : "))
    
    for i in range(Number):
        No = int(input("Enter input elements : "))
        
        Arr.append(No)
    
    Ret = AdditionOfList(Arr)
    
    print(f"Addition of all elements is : {Ret}")
    


if __name__ == "__main__":
    main()    