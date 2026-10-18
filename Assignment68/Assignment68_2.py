#----------------------------------------------------------------------------
# ReLU and Max Pooling
#----------------------------------------------------------------------------
# 1. Create Feature Map
# 2. Apply ReLU
# 3. Apply 2x2 Max Pooling
# 4. Display Output After Each Step
# 5. Explain Pooling
#----------------------------------------------------------------------------

border = "-" * 65

#----------------------------------------------------------------------------
# 1. Create Feature Map
#----------------------------------------------------------------------------
print(border)
print("1. Input Feature Map")
print(border)

feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

for row in feature_map:
    print(row)

#----------------------------------------------------------------------------
# 2. Apply ReLU
#----------------------------------------------------------------------------
print(border)
print("2. Apply ReLU")
print(border)

relu_output = []

for row in feature_map:
    relu_row = []

    for value in row:
        if value < 0:
            relu_row.append(0)
        else:
            relu_row.append(value)

    relu_output.append(relu_row)

print("ReLU Output:")

for row in relu_output:
    print(row)

#----------------------------------------------------------------------------
# 3. Apply 2x2 Max Pooling
#----------------------------------------------------------------------------
print(border)
print("3. Apply 2x2 Max Pooling")
print(border)

pool_size = 2
stride = 2

rows = len(relu_output)
cols = len(relu_output[0])

pool_output = []

for i in range(0, rows - pool_size + 1, stride):
    pool_row = []

    for j in range(0, cols - pool_size + 1, stride):
        region = []

        for r in range(pool_size):
            for c in range(pool_size):
                region.append(relu_output[i + r][j + c])

        maximum = max(region)
        pool_row.append(maximum)

        print("Region:", region)
        print("Maximum Value:", maximum)

    pool_output.append(pool_row)

#----------------------------------------------------------------------------
# 4. Display Final Output
#----------------------------------------------------------------------------
print(border)
print("4. Max Pooling Output")
print(border)

for row in pool_output:
    print(row)

#----------------------------------------------------------------------------
# 5. Explain Pooling
#----------------------------------------------------------------------------
print(border)
print("5. Explanation")
print(border)

print("ReLU converts negative values into zero.")
print("Max Pooling selects the maximum value from each region.")
print("Pooling reduces feature map size and computation.")