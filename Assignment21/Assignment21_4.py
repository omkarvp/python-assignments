# Design a Python application that creates two threads.
# 	Thread 1 should compute the sum of elements from a list. 
# 	Thread 2 should compute the product of elements from the same list. 
# 	Return the results to the main thread and display them. 

 

import threading
from Assignment21_Module import DisplayModule

SumOfData = []
ProductOfData = []

def SumOfElement(Data,ResultData):
    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")

    Sum = 0

    for No in Data:
        Sum += No
    ResultData.append(Sum)
    return ResultData

def ProductOfElement(Data,ResultData):
    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")

    Mult = 1

    for No in Data:
        Mult *= No
    ResultData.append(Mult)
    return ResultData            

def main():
    DisplayModule()

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to extract Maximum and Minimum number : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)
    
    print("")

    
    tObjSum = threading.Thread(target=SumOfElement,args=(NumberDataInput,SumOfData))
    tObjProduct = threading.Thread(target=ProductOfElement,args=(NumberDataInput,ProductOfData))

    print("*"*100)

    tObjSum.start()
    tObjProduct.start()
    
    tObjSum.join() # Main should wait until the job of tObjPrime completed 
    tObjProduct.join() # Main should wait until the job of tObjNonPrime completed

    print(SumOfData[0])
    print(ProductOfData[0])


if __name__ == "__main__":
    main()