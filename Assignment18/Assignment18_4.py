# Write a program which accept N numbers from user and store it into List. 
# Accept one another number from user and return frequency of that number from List.

# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

from Assignment18_Module import DisplayModule

def FrequencyOfNumber(SearchValue,Data):
    Counter = 0

    for No in Data:
        if No == SearchValue:
            Counter += 1
    return Counter

def main():
    DisplayModule()

    print("\n")

    Arr = list()

    Number = int(input("Enter number of elements : "))
    
    for i in range(Number):
        No = int(input("Enter input elements : "))
        
        Arr.append(No)

    SearchNumber = int(input("Enter number to get frequency of that number : "))    
    Ret = FrequencyOfNumber(SearchNumber,Arr)
    
    print(f"frequency of the number {SearchNumber} is : {Ret}")


if __name__ == "__main__":
    main()    