# 3. Use KNN to predict whether a student passes or fails based on study hours and attendance.
# Dataset
# Study Hours	Attendance	Result
# 2	60	Fail
# 5	80	Pass
# 6	85	Pass
# 1	50	Fail
# Tasks
# 1.	Accept input from the user: 
# o	Study hours 
# o	Attendance percentage 
# 2.	Apply the KNN algorithm. 
# 3.	Predict whether the student Passes or Fails. 
# Input Example
# Enter Study Hours: 4
# Enter Attendance: 70
# Expected Output
# Predicted Result: Pass


import math

border = "-"*65
def MarvellousUCDistance(P1,P2):
    Ans = math.sqrt((P1['Hours'] - P2['Hours']) ** 2 + (P1['Attendance'] - P2['Attendance']) ** 2)

    return Ans

def MarvellousKNNClassifier(Hours, Attendance):
        
    # Dataset
    Data = [
        {'Hours': 2, 'Attendance': 60, 'Result': 'Fail'},
        {'Hours': 5, 'Attendance': 80, 'Result': 'Pass'},
        {'Hours': 6, 'Attendance': 85, 'Result': 'Pass'},
        {'Hours': 1, 'Attendance': 50, 'Result': 'Fail'}
    ]

    
    new_point = {'Hours' : Hours, 'Attendance' : Attendance}

    for d in Data:
        d['distance'] = MarvellousUCDistance(d,new_point)

    sorted_data = sorted(Data,key=lambda item : item['distance'])

    k = 3

    nearest = sorted_data[:k]

    # voting
    votes = {}

    for neighbours in nearest:
        Result = neighbours['Result']
        votes[Result] = votes.get(Result,0) + 1

    iMax = 0
    Point = ""

    for d in votes:
        if votes[d] > iMax:
            iMax = votes[d]
            Point = d

    print("Predicted Class : ",Point)

def main():
    # Accept input from the user
    X = int(input("Enter Study Hours: "))
    Y = int(input("Enter Attendance: "))

    MarvellousKNNClassifier(X,Y)


if __name__ == "__main__":
    main()