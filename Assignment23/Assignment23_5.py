# 5: Write a program that calculates factorials of multiple numbers simultaneously using multiprocessing.Pool.
# Input
# Data = [10, 15, 20, 25]
# Expected Task
# For every N, calculate:
# N!
# Expected Output Format
# Process ID : 1240
# Input Number : 20
# Factorial : 2432902008176640000

import os
import multiprocessing
import time

from Assignment23_Module import DisplayModule


def Factorials(No):
    Factorial = 1
    for i in range(1, No + 1):
        Factorial *= i
    return {
        "pid": os.getpid(),
        "number": No,
        "factorial": Factorial
    }

def main():
    DisplayModule()

    print(f"The Process ID is : {os.getpid()}")

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to calculates factorials of multiple numbers simultaneously : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)

    start_time = time.perf_counter()
    result = list()

    p = multiprocessing.Pool()

    result = p.map(Factorials,NumberDataInput)

    p.close()
    p.join()
    end_time = time.perf_counter()
    lengthOfList = len(NumberDataInput)
    print("-"*40)
    for i in range(lengthOfList):
        print(f"Process ID is : {result[i]['pid']}")
        print(f"Input Number is : {result[i]['number']}")
        print(f"Factorial is : {result[i]['factorial']}")
        print("-"*40)

    TotalExecutionTime = end_time - start_time
    print(f"total execution time is : {TotalExecutionTime:.5f}")

if __name__ == "__main__":
    main()