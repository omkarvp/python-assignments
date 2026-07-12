# 2: Write a Python program using multiprocessing.Pool to calculate the sum of all odd numbers from 1 to n.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task
# For each number N, calculate:
# 1 + 3 + 5 + ... + N
# Expected Output Format
# Process ID : 1235
# Input Number : 1000000
# Sum of Odd Numbers : 250000000000


import os
import multiprocessing
import time
from Assignment23_Module import DisplayModule

def SumOfOddNumbers(No):
    print(f"The Process ID is : {os.getpid()}")
    
    SumOfOdd = 0
    
    for i in range(1,No+1):
        if i % 2 != 0:
            SumOfOdd += i

    return SumOfOdd



def main():
    DisplayModule()

    print(f"The Process ID is : {os.getpid()}")

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to calculate the sum of all Odd numbers : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)

    start_time = time.perf_counter()
    result = list()

    p = multiprocessing.Pool()

    result = p.map(SumOfOddNumbers,NumberDataInput)

    p.close()
    p.join()
    end_time = time.perf_counter()
    print(f"The sum of all Odd numbers is : {result}")
    TotalExecutionTime = end_time - start_time
    print(f"total execution time is : {TotalExecutionTime:.5f}")

if __name__ == "__main__":
    main()