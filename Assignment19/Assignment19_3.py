# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user. 
# Filter should filter out all such numbers which are greater than or equal to 70 and less than or equal to 90. 
# Map function will increase each number by 10. 
# Reduce will return product of all that numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000

from functools import reduce
from Assignment19_Module import DisplayModule

def FilterNumber(Number):
    if Number >= 70 and Number <= 90:
        return True
    
    return False

def MapIncreaseNumber(Number):
    return Number + 10

def ReduceNumber(Number1, Number2):
    return Number1 * Number2

def main():
    DisplayModule()

    print("\n")
    
    Arr = list()

    Number = int(input("Enter number of elements : "))
    
    for i in range(Number):
        No = int(input("Enter input elements : "))
        
        Arr.append(No)
    
    FData = list(filter(FilterNumber,Arr))
    
    print("\n")
    print(f"List after filter : {FData} ")

    MData = list(map(MapIncreaseNumber,FData))
    
    print("\n")
    print(f"List after map : {FData} ")

    Ret = reduce(ReduceNumber,MData)

    print("\n")
    print("Product of all that numbers is : {Ret}")

if __name__ == "__main__":
    main()