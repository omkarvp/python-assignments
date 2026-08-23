# 3.	Write a Python program using StandardScaler to perform feature scaling on the following dataset:
# [[25, 20000],
#  [30, 40000],
#  [35, 80000]]
# Print the scaled dataset.


import numpy as np
from sklearn.preprocessing import StandardScaler

border = "-" * 65


# Step 1
# ---------------------------------------------------
# Function Name : LoadData
# Description : Load the dataset
# Input : None
# Output : Dataset
# ---------------------------------------------------

def LoadData():

    X = [
        [25, 20000],
        [30, 40000],
        [35, 80000]
    ]

    print("Original Dataset : ")
    print(X)

    return X


# Step 2
# ---------------------------------------------------
# Function Name : ScaleData
# Description : Perform feature scaling using StandardScaler
# Input : Dataset
# Output : Scaled Dataset
# ---------------------------------------------------

def ScaleData(X):

    scaler = StandardScaler()

    X_scaled = scaler.fit_transform(X)

    print("Scaled Dataset : ")
    print(X_scaled)


def main():

    X = LoadData()

    ScaleData(X)


if __name__ == "__main__":
    main()
