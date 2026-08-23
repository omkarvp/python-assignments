# 2.	Write a Python program that calculates the variance and standard deviation of the dataset:
# [6, 7, 8, 9, 10, 11, 12]

import numpy as np

border = "-" * 65


# Step 1
# ---------------------------------------------------
# Function Name : LoadData
# Description : Load the dataset
# Input : None
# Output : Dataset
# ---------------------------------------------------

def LoadData():

    X = [6, 7, 8, 9, 10, 11, 12]

    print("Dataset : ", X)

    return X


# Step 2
# ---------------------------------------------------
# Function Name : CalculateVariance
# Description : Calculate variance using NumPy
# Input : Dataset
# Output : Variance
# ---------------------------------------------------

def CalculateVariance(X):

    Variance = np.var(X)

    print("Variance : ", Variance)

    return Variance


# Step 3
# ---------------------------------------------------
# Function Name : CalculateStandardDeviation
# Description : Calculate standard deviation using NumPy
# Input : Dataset
# Output : Standard Deviation
# ---------------------------------------------------

def CalculateStandardDeviation(X):

    StandardDeviation = np.std(X)

    print("Standard Deviation : ", StandardDeviation)


def main():

    X = LoadData()

    CalculateVariance(X)

    CalculateStandardDeviation(X)


if __name__ == "__main__":
    main()
