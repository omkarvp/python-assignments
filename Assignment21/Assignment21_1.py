# Design a Python application that creates two threads named Prime and NonPrime.
# 	Both threads should accept a list of integers. 
# 	The Prime thread should display all prime numbers from the list. 
# 	The NonPrime thread should display all non-prime numbers from the list. 

import threading
from Assignment21_Module import DisplayModule

def isPrime(Number):
    if Number <= 1:
        return False
    
    if Number == 2:
        return True

    if Number % 2 == 0:
        return False

    for i in range(2, Number):
        if Number % i == 0:
            return False

    return True
    


def Prime(Data):
    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")

    StringOfPrimeNumber = ""

    ListOfPrimeNumber = list()

    for No in Data:
        Ret = isPrime(No)
        if Ret == True:
            StringOfPrimeNumber += str(No) + " "
            ListOfPrimeNumber.append(No)

    print(f"All Prime numbers from the list using string : {StringOfPrimeNumber} and using List is : {ListOfPrimeNumber}")

def NonPrime(Data):
    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")
    
    StringOfNonPrimeNumber = ""
    
    ListOfNonPrimeNumber = list()
    
    for No in Data:
        Ret = isPrime(No)
        if Ret == False:
            StringOfNonPrimeNumber += str(No) + " "
            ListOfNonPrimeNumber.append(No)
    print(f"All NonPrime numbers from the list using string : {StringOfNonPrimeNumber} and using List is : {ListOfNonPrimeNumber}")
            

def main():
    DisplayModule()

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to extract prime numbers and non-prime numbers : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)
    
    print("")


    tObjPrime = threading.Thread(target=Prime,args=(NumberDataInput,))
    tObjNonPrime = threading.Thread(target=NonPrime,args=(NumberDataInput,))

    print("*"*100)

    tObjPrime.start()
    tObjNonPrime.start()
    
    tObjPrime.join() # Main should wait until the job of tObjPrime completed 
    tObjNonPrime.join() # Main should wait until the job of tObjNonPrime completed

if __name__ == "__main__":
    main()