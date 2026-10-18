#----------------------------------------------------------------------------
# Deep Learning Assignment :
#----------------------------------------------------------------------------
# 2: Write a Python program to demonstrate different activation functions.
# Functions to implement:
# 1. Sigmoid
# 2. ReLU
# 3. Tanh
# Tasks:
# 1. Accept input values from -10 to 10.
# 2. Plot all activation functions using Matplotlib.
# 3. Explain the use of each activation function.
#----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt

# 1. Accept input values from -10 to 10
x = np.linspace(-10, 10, 100)

# 2. Define activation functions
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def relu(x):
    return np.maximum(0, x)

def tanh(x):
    return np.tanh(x)

# 3. Calculate activation values
y_sigmoid = sigmoid(x)
y_relu = relu(x)
y_tanh = tanh(x)

# 4. Plot all activation functions
plt.figure(figsize=(10, 6))

plt.plot(x, y_sigmoid, label="Sigmoid")
plt.plot(x, y_relu, label="ReLU")
plt.plot(x, y_tanh, label="Tanh")

plt.title("Different Activation Functions")
plt.xlabel("Input")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.show()

# 5. Explain the use of each function
print("1. Sigmoid:")
print("It is commonly used in the output layer for binary classification.")
print("Converts values into a range between 0 and 1.")

print("\n2. ReLU:")
print("It is commonly used in hidden layers of neural networks.")
print("Returns 0 for negative inputs and x for positive inputs.")

print("\n3. Tanh:")
print("It is commonly used in hidden layers in some neural networks.")
print("Converts values into a range between -1 and 1.")