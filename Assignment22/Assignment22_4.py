# 4. Write a program that calculates
# 1^5 + 2^5 + 3^5 + ..... + N^5
# for multiple values of N simultaneously using Pool.
# Input
# [
#  1000000,
#  2000000,
#  3000000,
#  4000000
# ]
# Measure total execution time.


import multiprocessing
import time
import os

from Assignment22_Module import DisplayModule

def SumOfPowerofFive(No):
    print(f"The Process ID is : {os.getpid()}")
    
    SumOfPower = 0
    
    for i in range(1,No+1):
        SumOfPower += i ** 5

    return SumOfPower



def main():
    DisplayModule()

    print(f"The Process ID is : {os.getpid()}")

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to calculates Sum of power of 5 : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)

    start_time = time.perf_counter()
    result = list()

    p = multiprocessing.Pool()

    result = p.map(SumOfPowerofFive,NumberDataInput)

    p.close()
    p.join()
    end_time = time.perf_counter()
    print(f"Sum of Power of 5 for list {NumberDataInput} is : {result}")
    TotalExecutionTime = end_time - start_time
    print(f"total execution time is : {TotalExecutionTime:.5f}")




if __name__ == "__main__":
    main()