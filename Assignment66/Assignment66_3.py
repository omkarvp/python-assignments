#----------------------------------------------------------------------------
# Deep Learning Assignment :
#----------------------------------------------------------------------------
# 3: Write a Python program to calculate loss manually.
# Tasks:
# 1. Implement Mean Squared Error.
# 2. Implement Binary Cross Entropy.
# 3. Take actual and predicted values.
# 4. Display the calculated loss.
# 5. Explain which loss function is used for regression and classification.
#----------------------------------------------------------------------------
import math

# 1. Mean Squared Error (MSE)
def Marvellous_MSE(Y_True, Y_Pred):
    n = len(Y_Pred)
    total_error = 0

    for i in range(n):
        error = Y_True[i] - Y_Pred[i]
        total_error = total_error + (error ** 2)

    MSE = total_error / n
    return MSE


# 2. Binary Cross Entropy (BCE)
def Marvellous_BCE(Y_True, Y_Pred):
    n = len(Y_Pred)
    total_error = 0
    epsilon = 1e-15

    for i in range(n):
        pred = max(epsilon, min(Y_Pred[i], 1 - epsilon))

        error = (
            Y_True[i] * math.log(pred)
            + (1 - Y_True[i]) * math.log(1 - pred)
        )

        total_error = total_error + error

    BCE = -total_error / n
    return BCE


# Actual and Predicted values
Y_True = [1, 0, 1, 1, 0]
Y_Pred = [0.9, 0.2, 0.8, 0.7, 0.1]

# Calculate MSE Loss
loss = Marvellous_MSE(Y_True, Y_Pred)
print("Mean Squared Error Loss is:", loss)

# Calculate BCE Loss
loss = Marvellous_BCE(Y_True, Y_Pred)
print("Binary Cross Entropy Loss is:", loss)

# 3. Explanation
print("MSE is used for Regression.")
print("BCE is used for Binary Classification.")