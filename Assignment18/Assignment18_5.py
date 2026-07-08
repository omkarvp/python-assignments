# Write a program which accept N numbers from user and store it into List. 
# Return addition of all prime numbers from that List. 
# Main python file accepts N numbers from user and pass each number to ChkPrime() function 
# which is part of our user defined module named as MarvellousNum. 
# Name of the function from main python file should be ListPrime().

# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8

# Output : 32 (13 + 5 + 7 + 2 + 5)

from Assignment18_Module import DisplayModule
from MarvellousNum import ChkPrime

# Strpattern = "2 + 3 + "
# Strpattern = Strpattern.rstrip("+ ")
# print(Strpattern)

def ListPrime(Data):
    Sum = 0
    StrOfPrimeNumbers = ""
    for No in Data:
        isPrime = ChkPrime(No)
        if isPrime == True:
            Sum += No
            StrOfPrimeNumbers += str(No) + " + "
        
    StrOfPrimeNumbers = StrOfPrimeNumbers.rstrip("+ ")
    
    StrOfPrimeNumbers = str(Sum) + " (" + StrOfPrimeNumbers + ")"
    
    return StrOfPrimeNumbers

def main():
    DisplayModule()

    print("\n")

    Arr = list()

    Number = int(input("Enter number of elements : "))
    
    for i in range(Number):
        No = int(input("Enter input elements : "))
        
        Arr.append(No)

    Ret = ListPrime(Arr)
    
    print(f"Addition of Prime numbers is : {Ret}")


if __name__ == "__main__":
    main()    