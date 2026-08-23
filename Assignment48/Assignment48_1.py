# 1. Implement Simple Linear Regression manually without using any ML library.
# Dataset:
# X = [1, 2, 3, 4, 5]
# Y = [3, 4, 2, 4, 5]
# Tasks
# Calculate:
# 1.	Mean of X (X̄) 
# 2.	Mean of Y (Ȳ) 
# 3.	Slope (m) 
# 4.	Intercept (c) 
# Expected Output Example
# Mean of X = 3
# Mean of Y = 3.6
# Slope (m) = 0.4
# Intercept (c) = 2.4
# Regression Equation:
# Y = 0.4X + 2.4
# Predicted Y for X = 6 : 4.8


border = "-" * 65


# Step 1
# ---------------------------------------------------
# Function Name : LoadData
# Description : Load the data
# Input : None
# Output : X, Y
# ---------------------------------------------------

def LoadData():

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print("Independent variables : ", X)
    print("Dependent variables : ", Y)

    return X, Y


# Step 2
# ---------------------------------------------------
# Function Name : CalculateMean
# Description : Calculate mean of X and Y
# Input : X, Y
# Output : mean_x, mean_y
# ---------------------------------------------------

def CalculateMean(X, Y):

    sum_x = 0
    sum_y = 0

    for i in range(len(X)):
        sum_x = sum_x + X[i]
        sum_y = sum_y + Y[i]

    mean_x = sum_x / len(X)
    mean_y = sum_y / len(Y)

    print("Mean of X : ", mean_x)
    print("Mean of Y : ", mean_y)

    return mean_x, mean_y


# Step 3
# ---------------------------------------------------
# Function Name : CalculateSlope
# Description : Calculate slope of regression line
# Input : X, Y, mean_x, mean_y
# Output : Slope
# ---------------------------------------------------

def CalculateSlope(X, Y, mean_x, mean_y):

    numerator = 0
    denominator = 0

    for i in range(len(X)):

        numerator = numerator + (
            (X[i] - mean_x) * (Y[i] - mean_y)
        )

        denominator = denominator + (
            (X[i] - mean_x) ** 2
        )

    m = numerator / denominator

    print("Slope (m) : ", m)

    return m


# Step 4
# ---------------------------------------------------
# Function Name : CalculateIntercept
# Description : Calculate intercept
# Input : mean_x, mean_y, slope
# Output : Intercept
# ---------------------------------------------------

def CalculateIntercept(mean_x, mean_y, m):

    c = mean_y - (m * mean_x)

    print("Intercept (c) : ", c)

    return c


# Step 5
# ---------------------------------------------------
# Function Name : Predict
# Description : Predict Y for X = 6
# Input : X, slope, intercept
# Output : Predicted Y
# ---------------------------------------------------

def Predict(x, m, c):

    y = m * x + c

    print("Predicted Y for X = 6 : ", y)


# Main Function
# ---------------------------------------------------

def main():

    X, Y = LoadData()

    mean_x, mean_y = CalculateMean(X, Y)

    m = CalculateSlope(
        X,
        Y,
        mean_x,
        mean_y
    )

    c = CalculateIntercept(
        mean_x,
        mean_y,
        m
    )

    print("Regression Equation : Y =", m, "X +", c)

    Predict(6, m, c)


if __name__ == "__main__":
    main()
