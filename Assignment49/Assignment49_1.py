# 1.	Write a Python program that calculates the mean of a dataset using NumPy for the following values:
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
# Function Name : CalculateMean
# Description : Calculate mean using NumPy
# Input : Dataset
# Output : Mean
# ---------------------------------------------------

def CalculateMean(X):

    Mean = np.mean(X)

    print("Mean of dataset : ", Mean)


def main():

    X = LoadData()

    CalculateMean(X)


if __name__ == "__main__":
    main()
