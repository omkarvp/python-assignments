# 2. Write a program that calculates factorials of multiple numbers simultaneously using Pool.map().
# every element in the list.
# Example Input = [10, 15, 20, 25]
# Display
#	Process ID 
#	Input Number 
#	Factorial 

import multiprocessing
import os

from Assignment22_Module import DisplayModule

def Factorials(No):
    print(f"The Process ID is : {os.getpid()}")
    
    FactorialNumbers = 1
    
    for i in range(1,No+1):
        FactorialNumbers = FactorialNumbers*i

    return FactorialNumbers



def main():
    DisplayModule()

    print(f"The Process ID is : {os.getpid()}")

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to calculates factorials of multiple numbers simultaneously : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)

    result = list()

    p = multiprocessing.Pool()

    result = p.map(Factorials,NumberDataInput)

    p.close()
    p.join()

    print(f"Factorials of {NumberDataInput} simultaneously : {result}")




if __name__ == "__main__":
    main()