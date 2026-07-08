# Write a program which accept N numbers from user and store it into List. 
# Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to ChkPrime() function 
# which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 7 45 7 4 56 10 34 2 5 8
# Output : 34 (13 + 5 + 7 + 2 + 5)

from MarvellousNum import ChkPrime
from functools import reduce
from Assignment19_Module import DisplayModule


def ListPrime(Data):
    FData = list(filter(ChkPrime,Data))

    return FData

def ReduceAdditionOfPrimeNumber(Number1, Number2):
    return Number1 + Number2


def main():
    DisplayModule()

    print("\n")
    
    Arr = list()

    Number = int(input("Enter number of elements : "))
    
    for i in range(Number):
        No = int(input("Enter input elements : "))
        
        Arr.append(No)
    
    FData = ListPrime(Arr)
    
    print("\n")
    print(f"List after filter : {FData} ")
    
    Ret = reduce(ReduceAdditionOfPrimeNumber,FData)
    
    StrOfNumberAddition = ""
    
    for No in FData:
        StrOfNumberAddition += str(No)+" + "
    
    StrOfNumberAddition = StrOfNumberAddition.rstrip("+ ")

    print(f"Addition of all that numbers is : {Ret} ({StrOfNumberAddition})")

if __name__ == "__main__":
    main()