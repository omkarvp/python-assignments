# 3: Write a program that counts how many even numbers exist between 1 and n using pool.map().
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Output Format
# Process ID : 1236
# Input Number : 1000000
# Even Number Count : 500000


import os
import multiprocessing
import time
from Assignment23_Module import DisplayModule

def CountOfEvenNumbers(No):
    print(f"The Process ID is : {os.getpid()}")
    
    CountOfEven = 0
    
    for i in range(1,No+1):
        if i % 2 == 0:
            CountOfEven += 1

    return CountOfEven



def main():
    DisplayModule()

    print(f"The Process ID is : {os.getpid()}")

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to calculate the Count of all even numbers : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)

    start_time = time.perf_counter()
    result = list()

    p = multiprocessing.Pool()

    result = p.map(CountOfEvenNumbers,NumberDataInput)

    p.close()
    p.join()
    end_time = time.perf_counter()
    print(f"The Count of all even numbers is : {result}")
    TotalExecutionTime = end_time - start_time
    print(f"total execution time is : {TotalExecutionTime:.5f}")

if __name__ == "__main__":
    main()