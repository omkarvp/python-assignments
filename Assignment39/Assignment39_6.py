# 6. Train three Decision Tree models with:
# •	max_depth = 1 
# •	max_depth = 3 
# •	max_depth = None 
# Compare their testing accuracies and write your observations.


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

modelOne = DecisionTreeClassifier(max_depth=1, random_state=42)
modelThree = DecisionTreeClassifier(max_depth=3, random_state=42)
modelNone = DecisionTreeClassifier(max_depth=None, random_state=42)

print("Model gets created successfully")


########################################################
# Step - 5 : Train the model
########################################################

print(Border)
print("Step - 5 : Train the model")
print(Border)

modelOne.fit(X_train,Y_train)
modelThree.fit(X_train,Y_train)
modelNone.fit(X_train,Y_train)

print("Model trained successfully")

########################################################
# Step - 6 : Evaluate/Test the model
########################################################

print(Border)
print("Step - 6 : Evaluate/Test the model")
print(Border)

Y_predOne = modelOne.predict(X_test)
Y_predThree = modelThree.predict(X_test)
Y_predNone = modelNone.predict(X_test)

print("Model testing done")

########################################################
# Step - 7 : Evaluate the modele performance
########################################################

print(Border)
print("Step - 7 : Evaluate the modele performance")
print(Border)

# Accuracy
accuracyOne = accuracy_score(Y_test, Y_predOne)
accuracyThree = accuracy_score(Y_test, Y_predThree)
accuracyNone = accuracy_score(Y_test, Y_predNone)

print("Testing Accuracy (max_depth=1): {:.2f}%".format(accuracyOne * 100))
print("Testing Accuracy (max_depth=3): {:.2f}%".format(accuracyThree * 100))
print("Testing Accuracy (max_depth=None): {:.2f}%".format(accuracyNone * 100))
