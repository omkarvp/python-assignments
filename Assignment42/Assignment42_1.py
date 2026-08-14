# 1. Write a Python program that classifies a new data point using the K-Nearest Neighbors algorithm.
# The algorithm should be implemented manually without using any machine learning library.
# The program should:
# •	Calculate Euclidean distance 
# •	Sort distances 
# •	Select K nearest neighbors 
# •	Predict the class based on majority voting 
# Dataset
# Point	X	Y	Label
# A	1	2	Red
# B	2	3	Red
# C	3	1	Blue
# D	6	5	Blue
# Tasks
# 1.	Accept X and Y coordinates of a new point from the user. 
# 2.	Compute Euclidean distance from all dataset points. 
# 3.	Sort the distances. 
# 4.	Select K = 3 nearest neighbors. 
# 5.	Predict the class label.
# Input Format
# Enter X coordinate: 2
# Enter Y coordinate: 2
# Expected Output
# Nearest Neighbors:
# A - Distance: 1.0
# B - Distance: 1.0
# C - Distance: 1.41

# Predicted Class: Red

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

    k=3

    nearest = sorted_data[:k]

    print(border)
    print("Nearest 3 members are : ")
    print(border)
    for d in nearest:
        print(d['Point'], "- Distance: ", f"{d['distance']:.2f}")

    print(border)

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