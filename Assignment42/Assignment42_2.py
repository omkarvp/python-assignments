# 2. The value of K plays an important role in the KNN algorithm.
# Write a Python program that demonstrates how prediction changes when K changes.
# Dataset
# Use the same dataset as Assignment 1:
# Point	X	Y	Label
# A	    1	2	Red
# B	    2	3	Red
# C	    3	1	Blue
# D	    6	5	Blue
# Task
# Predict the class of the same new point (2, 2) using:
# •	K = 1 
# •	K = 3 
# •	K = 5 
# Note: The dataset has only 4 points, so K = 5 is not valid unless the program handles this case (for example, by displaying an error).


# Expected Output
# Prediction Results
# K = 1 → Red
# K = 3 → Red
# K = 5 → Blue
# Explain why the prediction changes when K increases.


import math

border = "-"*65
def MarvellousUCDistance(P1,P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)

    return Ans

def MarvellousKNNClassifier(X,Y):
        
    # Dataset
    Data = [
        {'Point': 'A', 'X': 1, 'Y': 2, 'label': 'Red'},
        {'Point': 'B', 'X': 2, 'Y': 3, 'label': 'Red'},
        {'Point': 'C', 'X': 3, 'Y': 1, 'label': 'Blue'},
        {'Point': 'D', 'X': 6, 'Y': 5, 'label': 'Blue'}
    ]

    new_point = {'X' : X, 'Y' : Y}

    for d in Data:
        d['distance'] = MarvellousUCDistance(d,new_point)

    sorted_data = sorted(Data,key=lambda item : item['distance'])

    kValues = [1,3,5]
    
    for k in kValues:
        if k > len(sorted_data):
            print("K =", k, "is invalid")
            continue

        nearest = sorted_data[:k]

        # voting
        votes = {}

        for neighbours in nearest:
            label = neighbours['label']
            votes[label] = votes.get(label,0) + 1

        iMax = 0
        Point = ""

        for d in votes:
            if votes[d] > iMax:
                iMax = votes[d]
                Point = d

        print("Predicted Class : ",Point)

def main():
    # Accept input from the user
    X = float(input("Enter X coordinate: "))
    Y = float(input("Enter Y coordinate: "))

    MarvellousKNNClassifier(X,Y)


if __name__ == "__main__":
    main()