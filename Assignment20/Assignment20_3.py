# Design a Python application that creates two threads named EvenList and OddList.
# •	Both threads should accept a list of integers as input. 
# •	The EvenList thread should: 
#   o	Extract all even elements from the list. 
#   o	Calculate and display their sum. 
# •	The OddList thread should: 
#   o	Extract all odd elements from the list. 
#   o	Calculate and display their sum. 
# •	Threads should run concurrently.



import threading
from Assignment20_Module import DisplayModule

def SumOfOnlyEvenNumbersFromList(Data):
    print("\n")
    print(f"From SumOfFactorOfEvenNumbers function The Thread id is : {threading.get_ident()}")
    SumOfEvenNumbers = 0
    StringOfEvenNumber = ""

    for No in Data:
        if No % 2 == 0:
            SumOfEvenNumbers += No
            StringOfEvenNumber += str(No) + " "

    print("\n")
    print(f"Extracted Even numbers from {Data} are : {StringOfEvenNumber} and Sum is : {SumOfEvenNumbers}")

def SumOfOnlyOddNumbersFromList(Data):
    print("\n")
    print(f"From SumOfFactorOfOddNumbers function The Thread id is : {threading.get_ident()}")
    SumOfOddNumbers = 0
    StringOfOddNumber = ""
    
    for No in Data:
        if No % 2 != 0:
            SumOfOddNumbers += No
            StringOfOddNumber += str(No) + " "

    print("\n")
    print(f"Extracted Odd numbers from {Data} are : {StringOfOddNumber} and Sum is : {SumOfOddNumbers}")

def main():
    DisplayModule()

    EvenNumberDataInput = list()
    OddNumberDataInput = list()

    EvenNumberLength = int(input("Enter number of elements to extract even numbers and get sum : "))
    
    for i in range(EvenNumberLength):
        EvenInputList = int(input("Enter input elements : "))

        EvenNumberDataInput.append(EvenInputList)

    OddNumberLength = int(input("Enter number of elements to extract odd numbers and get sum : "))
    
    for i in range(OddNumberLength):
        OddInputList = int(input("Enter input elements : "))

        OddNumberDataInput.append(OddInputList)
    
    tObjEven = threading.Thread(target=SumOfOnlyEvenNumbersFromList,args=(EvenNumberDataInput,))
    tObjOdd = threading.Thread(target=SumOfOnlyOddNumbersFromList,args=(OddNumberDataInput,))

    tObjEven.start()
    tObjOdd.start()

    tObjEven.join() # Main should wait until the job of tObjEven completed 
    tObjOdd.join() # Main should wait until the job of tObjOdd completed

if __name__ == "__main__":
    main()