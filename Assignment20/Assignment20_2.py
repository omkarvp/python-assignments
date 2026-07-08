# Design a Python application that creates two threads named EvenFactor and OddFactor.
# •	Both threads should accept one integer number as a parameter. 
# •	The EvenFactor thread should: 
#   o	Identify all even factors of the given number. 
#   o	Calculate and display the sum of even factors. 
# •	The OddFactor thread should: 
#   o	Identify all odd factors of the given number. 
#   o	Calculate and display the sum of odd factors. 
# •	After both threads complete execution, the main thread should display the message: 
#   o	"Exit from main"


import threading
from Assignment20_Module import DisplayModule

def SumOfFactorOfEvenNumbers(RangeNum):
    print("\n")
    print(f"From SumOfFactorOfEvenNumbers function The Thread id is : {threading.get_ident()}")
    SumOfEvenFactors = 0
    StringOfEvenNumber = ""
    for i in range(1,RangeNum+1):
        if RangeNum % i == 0 and i % 2 == 0:
            SumOfEvenFactors += i 
            StringOfEvenNumber += str(i) + " "

    print("\n")
    print(f"Even Factors for {RangeNum} are : {StringOfEvenNumber} and Sum is : {SumOfEvenFactors}")

def SumOfFactorOfOddNumbers(RangeNum):
    print("\n")
    print(f"From SumOfFactorOfOddNumbers function The Thread id is : {threading.get_ident()}")
    SumOfOddFactors = 0
    StringOfOddNumber = ""
    for i in range(1, RangeNum+1):
        if RangeNum % i == 0 and i % 2 != 0:
            SumOfOddFactors += i
            StringOfOddNumber += str(i) + " "

    print("\n")
    print(f"Odd Factors for {RangeNum} are : {StringOfOddNumber} and Sum is : {SumOfOddFactors}")

def main():
    DisplayModule()
    Number1 = int(input("Enter the number to get sum of factors for even numbers : "))
    Number2 = int(input("Enter the number to get sum of factors for odd numbers : "))

    tObjEven = threading.Thread(target=SumOfFactorOfEvenNumbers,args=(Number1,))
    tObjOdd = threading.Thread(target=SumOfFactorOfOddNumbers,args=(Number2,))

    tObjEven.start()
    tObjOdd.start()

    tObjEven.join() # Main should wait until the job of tObjEven completed 
    tObjOdd.join() # Main should wait until the job of tObjOdd completed

if __name__ == "__main__":
    main()