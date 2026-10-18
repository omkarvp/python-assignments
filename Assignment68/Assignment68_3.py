#----------------------------------------------------------------------------
# Flattening in CNN
#----------------------------------------------------------------------------
# 1. Take a 2D Matrix
# 2. Convert Matrix into 1D Vector
# 3. Pass Vector to Fully Connected Layer
# 4. Calculate Final Output Manually
# 5. Explain Flatten Layer
#----------------------------------------------------------------------------

border = "-" * 65

#----------------------------------------------------------------------------
# 1. Take a 2D Matrix
#----------------------------------------------------------------------------
print(border)
print("1. Input Matrix")
print(border)

matrix = [
    [6, 4],
    [8, 6]
]

for row in matrix:
    print(row)

#----------------------------------------------------------------------------
# 2. Convert Matrix into 1D Vector
#----------------------------------------------------------------------------
print(border)
print("2. Flatten Output")
print(border)

flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)

print("Flatten Output:", flatten_output)

#----------------------------------------------------------------------------
# 3. Pass Vector to Fully Connected Layer
#----------------------------------------------------------------------------
print(border)
print("3. Fully Connected Layer")
print(border)

weights = [0.2, 0.3, 0.4, 0.5]
bias = 1

print("Input Vector:", flatten_output)
print("Weights:", weights)
print("Bias:", bias)

#----------------------------------------------------------------------------
# 4. Calculate Final Output Manually
#----------------------------------------------------------------------------
print(border)
print("4. Calculate Final Output")
print(border)

total = 0

for i in range(len(flatten_output)):
    multiplication = flatten_output[i] * weights[i]

    print(
        flatten_output[i], "*", weights[i],
        "=", multiplication
    )

    total = total + multiplication

final_output = total + bias

print("Weighted Sum:", total)
print("Final Output:", final_output)

#----------------------------------------------------------------------------
# 5. Explain Flatten Layer
#----------------------------------------------------------------------------
print(border)
print("5. Role of Flatten Layer")
print(border)

print("Flatten converts a 2D feature map into a 1D vector.")
print("The vector is passed to a fully connected layer.")
print("It helps CNN use extracted features for prediction.")