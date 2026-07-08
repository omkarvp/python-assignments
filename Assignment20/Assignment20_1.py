# Design a Python application that creates two separate threads named Even and Odd.
# •	The Even thread should display the first 10 even numbers. 
# •	The Odd thread should display the first 10 odd numbers. 
# •	Both threads should execute independently using the threading module. 
# •	Ensure proper thread creation and execution. 

import threading
from Assignment20_Module import DisplayModule

def EvenNumbers(RangeNum):
    print("\n")
    print(f"From EvenNumbers function The Thread id is : {threading.get_ident()}")
    StringOfEvenNumber = ""
    for i in range(2, RangeNum+1, 2):
        StringOfEvenNumber += str(i) + " "

    print("\n")
    print(f"First 10 Even Numbers : {StringOfEvenNumber}")

def OddNumbers(RangeNum):
    print("\n")
    print(f"From OddNumbers function The Thread id is : {threading.get_ident()}")
    StringOfOddNumber = ""
    for i in range(1, RangeNum, 2):
        StringOfOddNumber += str(i) + " "

    print("\n")
    print(f"First 10 Odd numbers : {StringOfOddNumber}")

def main():
    DisplayModule()

    tObjEven = threading.Thread(target=EvenNumbers,args=(20,))
    tObjOdd = threading.Thread(target=OddNumbers,args=(20,))

    tObjEven.start()
    tObjOdd.start()

    tObjEven.join() # Main should wait until the job of tObjEven completed 
    tObjOdd.join() # Main should wait until the job of tObjOdd completed

if __name__ == "__main__":
    main()