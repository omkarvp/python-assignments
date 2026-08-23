# 2. Using the same dataset from above question, calculate model performance.
# Tasks
# 1.	Predict all Y values using regression equation.
# 2.	Calculate:
# o	Mean Squared Error (MSE)
# o	R² Score
# Show all intermediate calculations.


from sklearn.metrics import mean_squared_error, r2_score

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

    return X, Y


# Step 2
# ---------------------------------------------------
# Function Name : PredictValues
# Description : Predict all Y values
# Input : X, slope, intercept
# Output : Predicted Y
# ---------------------------------------------------

def PredictValues(X, m, c):

    Y_pred = []

    for i in range(len(X)):

        Y = m * X[i] + c

        Y_pred.append(Y)

    print("Actual Y values : ", Y)
    print("Predicted Y values : ", Y_pred)

    return Y_pred


# Step 3
# ---------------------------------------------------
# Function Name : CalculateMSE
# Description : Calculate Mean Squared Error
# Input : Actual Y and Predicted Y
# Output : MSE
# ---------------------------------------------------

def CalculateMSE(Y, Y_pred):

    MSE = mean_squared_error(Y, Y_pred)

    print("Mean Squared Error (MSE) : ", MSE)

    return MSE


# Step 4
# ---------------------------------------------------
# Function Name : CalculateR2
# Description : Calculate R2 Score
# Input : Actual Y and Predicted Y
# Output : R2 Score
# ---------------------------------------------------

def CalculateR2(Y, Y_pred):

    R2 = r2_score(Y, Y_pred)

    print("R2 Score : ", R2)

    return R2


# Main Function
# ---------------------------------------------------

def main():

    X, Y = LoadData()

    m = 0.4
    c = 2.4

    Y_pred = PredictValues(X, m, c)

    CalculateMSE(Y, Y_pred)

    CalculateR2(Y, Y_pred)


if __name__ == "__main__":
    main()
