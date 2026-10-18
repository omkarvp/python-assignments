#----------------------------------------------------------------------------
# Manual Convolution
#----------------------------------------------------------------------------
# 1. Create Image Matrix
# 2. Create Kernel Matrix
# 3. Move Kernel Over Image
# 4. Perform Multiplication and Addition
# 5. Generate Feature Map
#----------------------------------------------------------------------------

border = "-" * 65

#----------------------------------------------------------------------------
# 1. Create Image Matrix
#----------------------------------------------------------------------------
print(border)
print("1. Input Image Matrix")
print(border)

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

for row in image:
    print(row)

#----------------------------------------------------------------------------
# 2. Create Kernel Matrix
#----------------------------------------------------------------------------
print(border)
print("2. Kernel Matrix")
print(border)

kernel = [
    [-1, -1, -1],
    [ 0,  0,  0],
    [ 1,  1,  1]
]

for row in kernel:
    print(row)

#----------------------------------------------------------------------------
# 3. Move Kernel Over Image
#----------------------------------------------------------------------------
print(border)
print("3. Move Kernel Over Image")
print(border)

image_size = len(image)
kernel_size = len(kernel)

feature_size = image_size - kernel_size + 1

feature_map = []

#----------------------------------------------------------------------------
# 4. Perform Multiplication and Addition
#----------------------------------------------------------------------------
print(border)
print("4. Region Calculations")
print(border)

for i in range(feature_size):
    feature_row = []

    for j in range(feature_size):
        total = 0
        calculation = []

        print("\nRegion Calculation:")

        for row in range(kernel_size):
            for col in range(kernel_size):
                image_value = image[i + row][j + col]
                kernel_value = kernel[row][col]

                result = image_value * kernel_value
                total = total + result

                calculation.append(
                    f"{image_value}*{kernel_value}"
                )

        print("Region:")
        for row in range(kernel_size):
            print(image[i + row][j:j + kernel_size])

        print("Calculation:")
        print(" + ".join(calculation))

        print("Output =", total)

        feature_row.append(total)

    feature_map.append(feature_row)

#----------------------------------------------------------------------------
# 5. Generate Feature Map
#----------------------------------------------------------------------------
print(border)
print("5. Final Feature Map")
print(border)

for row in feature_map:
    print(row)