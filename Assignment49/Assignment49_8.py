# 8.	Write a Python program that calculates TP, TN, FP, FN for the following arrays:
# actual   = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]
# Display all four values.

import numpy as np

border = "-" * 65


# Step 1
# ---------------------------------------------------
# Function Name : LoadData
# Description : Load actual and predicted values
# Input : None
# Output : Actual and Predicted values
# ---------------------------------------------------

def LoadData():

    actual = [1, 1, 1, 1, 0, 0, 0, 0]

    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    print("Actual values : ", actual)
    print("Predicted values : ", predicted)

    return actual, predicted


# Step 2
# ---------------------------------------------------
# Function Name : CalculateConfusionValues
# Description : Calculate TP, TN, FP and FN
# Input : Actual and Predicted values
# Output : TP, TN, FP, FN
# ---------------------------------------------------

def CalculateConfusionValues(actual, predicted):

    TP = 0
    TN = 0
    FP = 0
    FN = 0

    for i in range(len(actual)):

        if actual[i] == 1 and predicted[i] == 1:
            TP = TP + 1

        elif actual[i] == 0 and predicted[i] == 0:
            TN = TN + 1

        elif actual[i] == 0 and predicted[i] == 1:
            FP = FP + 1

        elif actual[i] == 1 and predicted[i] == 0:
            FN = FN + 1

    print("True Positive (TP) : ", TP)
    print("True Negative (TN) : ", TN)
    print("False Positive (FP) : ", FP)
    print("False Negative (FN) : ", FN)


def main():

    actual, predicted = LoadData()

    CalculateConfusionValues(
        actual,
        predicted
    )


if __name__ == "__main__":
    main()
