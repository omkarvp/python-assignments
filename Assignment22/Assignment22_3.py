# 3. For every number in the given list, count how many prime numbers exist between 1 and N using multiprocessing.Pool.
# Example
# 10000
# 20000
# 30000
# 40000
# Expected Task
# Display the total prime count for each number.
# For example, the output format could be:
# Input Number : 10000
# Prime Count  : 1229


import multiprocessing
import os

from Assignment22_Module import DisplayModule

def isPrimeNumber(Number):
    if Number <= 1:
        return False
    
    if Number == 2:
        return True
    
    if Number % 2 == 0:
        return False
    
    # Check divisibility from 2 to n-1
    for i in range(2, Number):
        if Number % i == 0:
            return False
     
    return True
def CountPrimenNumber(No):
    print(f"The Process ID is : {os.getpid()}")
    
    Count = 0
    
    for i in range(1,No+1):
        if isPrimeNumber(i):
            Count += 1

    return Count



def main():
    DisplayModule()

    print(f"The Process ID is : {os.getpid()}")

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to count how many prime numbers exist between 1 and N : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)

    result = list()

    p = multiprocessing.Pool()

    result = p.map(CountPrimenNumber,NumberDataInput)

    p.close()
    p.join()

    print(f"Prime Count {NumberDataInput} is : {result}")




if __name__ == "__main__":
    main()