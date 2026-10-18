#----------------------------------------------------------------------------
# Deep Learning Assignment :
#----------------------------------------------------------------------------
# 4: Write a Python program to show how weights are updated in ANN.
# Tasks:
# 1. Take input, weight, bias, target output, and learning rate.
# 2. Calculate prediction.
# 3. Calculate error.
# 4. Update weight using gradient descent logic.
# 5. Display old weight and updated weight.
#----------------------------------------------------------------------------
# Function to update weight using gradient descent
def Marvellous_Update_Weight(X, Weight, Bias, Y_True, Learning_Rate):

    # 1. Calculate prediction
    Y_Pred = (X * Weight) + Bias
    print("Prediction is:", Y_Pred)

    # 2. Calculate error
    Error = Y_True - Y_Pred
    print("Error is:", Error)

    # 3. Calculate gradient
    Gradient = -2 * X * Error

    # 4. Update weight
    Updated_Weight = Weight - (Learning_Rate * Gradient)

    return Updated_Weight


# Input values

X = float(input("Enter input: "))   # 2
Weight = float(input("Enter weight: ")) # 0.5
Bias = float(input("Enter bias: ")) # 0.1
Y_True = float(input("Enter target output: ")) # 1.0
Learning_Rate = float(input("Enter learning rate: ")) # 0.01

# Display old weight
print("Old Weight is:", Weight)

# Update weight
New_Weight = Marvellous_Update_Weight(
    X, Weight, Bias, Y_True, Learning_Rate
)

# Display updated weight
print("Updated Weight is:", New_Weight)