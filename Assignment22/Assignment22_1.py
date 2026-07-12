# 1. Write a program that accepts a list of integers and uses Pool.map() to calculate the sum of squares from 1 to N for 
# every element in the list.
# Example Input = [1000000, 2000000, 3000000, 4000000]
# Expected Output
# [
#     333333833333500000,
#     2666668666667000000,
#     ...
# ]

import multiprocessing

from Assignment22_Module import DisplayModule

def SumOfSquares(No):
    Sum = 0
    
    for i in range(1,No+1):
        Sum += i ** 2
    
    return Sum



def main():
    DisplayModule()

    NumberDataInput = list()

    NumberLength = int(input("Enter number of elements to calculate the sum of squares from 1 to N : "))
    
    for i in range(NumberLength):
        InputList = int(input("Enter input elements : "))

        NumberDataInput.append(InputList)

    result = list()

    p = multiprocessing.Pool()

    result = p.map(SumOfSquares,NumberDataInput)

    p.close()
    p.join()

    print(f"Sum of squres of elements : {result}")




if __name__ == "__main__":
    main()