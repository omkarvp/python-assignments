# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are even. 
# Map function will calculate its square. 
# Reduce will return addition of all that numbers.
# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204


from functools import reduce
from Assignment19_Module import DisplayModule

def FilterEvenNumber(Number):
    return Number % 2 == 0

def MapSquareOfNumber(Number):
    return Number ** 2

def ReduceAdditionOfNumber(Number1, Number2):
    return Number1 + Number2

def main():
    DisplayModule()

    print("\n")
    
    Arr = list()

    Number = int(input("Enter number of elements : "))
    
    for i in range(Number):
        No = int(input("Enter input elements : "))
        
        Arr.append(No)
    
    FData = list(filter(FilterEvenNumber,Arr))
    
    print("\n")
    print(f"List after filter : {FData} ")
    
    MData = list(map(MapSquareOfNumber,FData))
    
    print("\n")
    print(f"List after map : {FData} ")
    
    Ret = reduce(ReduceAdditionOfNumber,MData)
    
    print("\n")
    print(f"Addition of all that numbers is : {Ret} ")

if __name__ == "__main__":
    main()