# 1. Import DecisionTreeClassifier from sklearn.
# Create a model object and train it using fit().

import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

Border = "-"*65
#########################################
# Step - 1 : Load the Dataset
#########################################

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

print(Border)
print("Step - 1 : Load the Dataset")
print(Border)

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath) # df stands for Data Frame

print("Data set loaded successfully")

########################################################
# Step - 2 : Decide Indenpendent and Dependent Varibles
########################################################

print(Border)
print("Step - 2 : Decide Indenpendent and Dependent Varibles")
print(Border)


#x : Independent Variables / Features
#y : Dependent Variables / Labels

feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted",
    "SleepHours"
]

X = df[feature_cols]
Y = df["FinalResult"]

########################################################
# Step - 3 : Split the dataset for training and testing
########################################################

print(Border)
print("Step - 3 : Split the dataset for training and testing")
print(Border)

X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.5, random_state = 42)

print("Dataset spliting activity done")

########################################################
# Step - 4 : Build the model
########################################################

print(Border)
print("Step - 4 : Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model gets created successfully")


########################################################
# Step - 5 : Train the model
########################################################

print(Border)
print("Step - 5 : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model trained successfully")

########################################################
# Step - 6 : Evaluate/Test the model
########################################################

print(Border)
print("Step - 6 : Evaluate/Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model testing done")

########################################################
# Step - 7 : New DataFrame with details of 5 new students
########################################################

new_students = pd.DataFrame({
    "StudyHours": [2, 5, 7, 8, 3],
    "Attendance": [65, 82, 90, 95, 70],
    "PreviousScore": [45, 62, 70, 80, 50],
    "AssignmentsCompleted": [3, 6, 8, 9, 4],
    "SleepHours": [5, 7, 8, 8, 6]
})

print("New Students Details:")
print(new_students)


# Predict results

predictions = model.predict(new_students)


# Add predictions to DataFrame

new_students["PredictedResult"] = predictions


# Convert 0/1 into Fail/Pass

new_students["PredictedResult"] = new_students["PredictedResult"].map(
    {0: "Fail", 1: "Pass"}
)


print("\nPrediction Results:")
print(new_students)