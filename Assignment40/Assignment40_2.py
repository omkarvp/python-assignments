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
New_feature_cols = [
    "StudyHours",
    "Attendance",
    "PreviousScore",
    "AssignmentsCompleted"
]

X = df[feature_cols]
X_New = df[New_feature_cols]
Y = df["FinalResult"]

########################################################
# Step - 3 : Split the dataset for training and testing
########################################################

print(Border)
print("Step - 3 : Split the dataset for training and testing")
print(Border)

X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.5, random_state = 42)
X_New_train , X_New_test, Y_New_train, Y_New_test = train_test_split(X_New,Y,test_size = 0.5, random_state = 42)

print("Dataset spliting activity done")

########################################################
# Step - 4 : Build the model
########################################################

print(Border)
print("Step - 4 : Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)
modelNew = DecisionTreeClassifier(max_depth=5)

print("Model gets created successfully")


########################################################
# Step - 5 : Train the model
########################################################

print(Border)
print("Step - 5 : Train the model")
print(Border)

model.fit(X_train,Y_train)
modelNew.fit(X_New_train,Y_New_train)

print("Model trained successfully")

########################################################
# Step - 6 : Evaluate/Test the model
########################################################

print(Border)
print("Step - 6 : Evaluate/Test the model")
print(Border)

Y_pred = model.predict(X_test)
Y_New_pred = modelNew.predict(X_New_test)

print("Model testing done")

########################################################
# Step - 7 : Evaluate the modele performance
########################################################

print(Border)
print("Step - 7 : Evaluate the modele performance")
print(Border)


# Testing Prediction
test_pred = model.predict(X_test)
test_New_pred = modelNew.predict(X_New_test)

# Accuracy
test_accuracy = accuracy_score(Y_test, test_pred)
test_New_accuracy = accuracy_score(Y_New_test, test_New_pred)


print("Testing Old Accuracy: {:.2f}%".format(test_accuracy * 100))
print("Testing New Accuracy: {:.2f}%".format(test_New_accuracy * 100))