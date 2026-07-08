# Design a Python application that creates two threads.
# 	Thread 1 should calculate and display the maximum element from a list. 
# 	Thread 2 should calculate and display the minimum element from the same list. 
# 	The list should be accepted from the user. 
 

import threading
from Assignment21_Module import DisplayModule

def MaximumElement(Data):
    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")

    MaxElementUsingForLoop = Data[0]

    for No in Data:
        if MaxElementUsingForLoop < No:
            MaxElementUsingForLoop = No

    print(f"Maximum elements from the list using For loop : {MaxElementUsingForLoop}")

    print("")
    MaxElementUsingInbuiltFunction = max(Data)

    print(f"Maximum elements from the list using in-built function : {MaxElementUsingInbuiltFunction}")
    


def MinimumElement(Data):
    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")
    
    MinElementUsingForLoop = Data[0]

    for No in Data:
        if MinElementUsingForLoop > No:
            MinElementUsingForLoop = No

    print(f"Minimum elements from the list using For loop : {MinElementUsingForLoop}")

    print("")
    MaxElementUsingInbuiltFunction = min(Data)

    print(f"Minimum elements from the list using in-built function : {MaxElementUsingInbuiltFunction}")
            

def main():
    DisplayModule()

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to extract Maximum and Minimum number : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)
    
    print("")


    tObjPrime = threading.Thread(target=MaximumElement,args=(NumberDataInput,))
    tObjNonPrime = threading.Thread(target=MinimumElement,args=(NumberDataInput,))

    print("*"*100)

    tObjPrime.start()
    tObjNonPrime.start()
    
    tObjPrime.join() # Main should wait until the job of tObjPrime completed 
    tObjNonPrime.join() # Main should wait until the job of tObjNonPrime completed

if __name__ == "__main__":
    main()