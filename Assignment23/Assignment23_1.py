# 1: Write a Python program using multiprocessing.Pool to calculate the sum of all even numbers 
# from 1 to n for every number from the given list.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task
# For each number N, calculate:
# 2 + 4 + 6 + ... + N
# Expected Output Format
# Process ID : 1234
# Input Number : 1000000
# Sum of Even Numbers : 250000500000

import os
import multiprocessing
import time
from Assignment23_Module import DisplayModule

def SumOfEvenNumbers(No):
    print(f"The Process ID is : {os.getpid()}")
    
    SumOfEven = 0
    
    for i in range(1,No+1):
        if i % 2 == 0:
            SumOfEven += i

    return SumOfEven



def main():
    DisplayModule()

    print(f"The Process ID is : {os.getpid()}")

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to calculate the sum of all even numbers : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)

    start_time = time.perf_counter()
    result = list()

    p = multiprocessing.Pool()

    result = p.map(SumOfEvenNumbers,NumberDataInput)

    p.close()
    p.join()
    end_time = time.perf_counter()
    print(f"The sum of all even numbers is : {result}")
    TotalExecutionTime = end_time - start_time
    print(f"total execution time is : {TotalExecutionTime:.5f}")

if __name__ == "__main__":
    main()