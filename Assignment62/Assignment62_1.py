#----------------------------------------------------------------------------
# Deep Learning Assignment : Employee Attrition Prediction System
#----------------------------------------------------------------------------
# 1  . Read the data from CSV
# 2  . Display Shape, Columns and First 5 Records
# 3  . Check Missing Values
# 4  . Identify Numerical and Categorical Features
# 5  . Convert Categorical Features into Numerical
# 6  . Convert Target Attrition into 0 and 1
# 7  . Separate Independent and Dependent Variables
# 8  . Train Test Split
# 9  . Feature Scaling (Standard Scalar)
# 10 . Design MLP Model
# 11 . Train the Network
# 12 . Display Number of Iterations
# 13 . Calculate Training Accuracy
# 14 . Calculate Testing Accuracy
# 15 . Generate Confusion Matrix
# 16 . Plot Loss Curve
# 17 . Create PredictAttrition() Function
# 18 . Test Five New Employee Records
# 19 . Overfitting and Underfitting
#----------------------------------------------------------------------------
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

border = "-" * 75

#----------------------------------------------------------------------------
# 1 . Read the data from CSV
#----------------------------------------------------------------------------
print(border)
print("1 . Read the data from CSV")
print(border)

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
DataPath = parent_directory +"\\Employee_Attrition.csv"


data = pd.read_csv(DataPath)

print("Complete Dataset :")
print(data)

#----------------------------------------------------------------------------
# 2 . Display Shape, Columns and First 5 Records
#----------------------------------------------------------------------------
print(border)
print("2 . Display Shape, Columns and First 5 Records")
print(border)

print("Dataset Shape :")
print(data.shape)

print("Column Names :")
print(data.columns)

print("First 5 Records :")
print(data.head())

#----------------------------------------------------------------------------
# 3 . Check Missing Values
#----------------------------------------------------------------------------
print(border)
print("3 . Check Missing Values")
print(border)

print("Missing Values :")
print(data.isnull().sum())

for column in data.columns:
    if data[column].isnull().any():
        if data[column].dtype == "object":
            data[column] = data[column].fillna(data[column].mode()[0])
        else:
            data[column] = data[column].fillna(data[column].median())

print("Missing values handled successfully")

#----------------------------------------------------------------------------
# 4 . Identify Numerical and Categorical Features
#----------------------------------------------------------------------------
print(border)
print("4 . Identify Numerical and Categorical Features")
print(border)

numerical_features = data.select_dtypes(include=["number"]).columns
categorical_features = data.select_dtypes(include=["object"]).columns

print("Numerical Features :")
print(numerical_features)

print("Categorical Features :")
print(categorical_features)

#----------------------------------------------------------------------------
# 5 . Convert Categorical Features into Numerical
#----------------------------------------------------------------------------
print(border)
print("5 . Convert Categorical Features into Numerical")
print(border)

data["OverTime"] = data["OverTime"].map({
    "Yes": 1,
    "No": 0
})

print("OverTime converted into numerical representation")
print(data["OverTime"].head())

#----------------------------------------------------------------------------
# 6 . Convert Target Attrition into 0 and 1
#----------------------------------------------------------------------------
print(border)
print("6 . Convert Target Attrition into 0 and 1")
print(border)

data["Attrition"] = data["Attrition"].map({
    "Yes": 1,
    "No": 0
})

print("Attrition converted successfully")
print(data["Attrition"].head())

#----------------------------------------------------------------------------
# 7 . Separate Independent and Dependent Variables
#----------------------------------------------------------------------------
print(border)
print("7 . Separate Independent and Dependent Variables")
print(border)

X = data[
    [
        "Age",
        "MonthlyIncome",
        "YearsAtCompany",
        "TotalWorkingYears",
        "DistanceFromHome",
        "JobSatisfaction",
        "WorkLifeBalance",
        "OverTime",
        "NumCompaniesWorked",
        "TrainingTimesLastYear"
    ]
]

Y = data["Attrition"]

print("Independent Variables :")
print(X.head())

print("Dependent Variable :")
print(Y.head())

#----------------------------------------------------------------------------
# 8 . Train Test Split
#----------------------------------------------------------------------------
print(border)
print("8 . Train Test Split")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.3,
    random_state=42,
    stratify=Y
)

print("Training Input Shape :", X_train.shape)
print("Testing Input Shape :", X_test.shape)
print("Training Output Shape :", Y_train.shape)
print("Testing Output Shape :", Y_test.shape)

#----------------------------------------------------------------------------
# 9 . Feature Scaling (Standard Scalar)
#----------------------------------------------------------------------------
print(border)
print("9 . Feature Scaling (Standard Scalar)")
print(border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

print("Scaled Training Data :")
print(X_train_scaled[:5])

#----------------------------------------------------------------------------
# 10 . Design MLP Model
#----------------------------------------------------------------------------
print(border)
print("10 . Design MLP Model")
print(border)

model = MLPClassifier(
    hidden_layer_sizes=(16, 8),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42,
    early_stopping=True,
    validation_fraction=0.1,
    n_iter_no_change=20
)

print(model)
print("Two hidden layers created successfully")

#----------------------------------------------------------------------------
# 11 . Train the Network
#----------------------------------------------------------------------------
print(border)
print("11 . Train the Network")
print(border)

model.fit(X_train_scaled, Y_train)

print("Model trained successfully")

#----------------------------------------------------------------------------
# 12 . Display Number of Iterations
#----------------------------------------------------------------------------
print(border)
print("12 . Display Number of Iterations")
print(border)

print("Number of Iterations Required :", model.n_iter_)

#----------------------------------------------------------------------------
# 13 . Calculate Training Accuracy
#----------------------------------------------------------------------------
print(border)
print("13 . Calculate Training Accuracy")
print(border)

Y_train_pred = model.predict(X_train_scaled)

train_accuracy = accuracy_score(Y_train, Y_train_pred)

print("Training Accuracy :", train_accuracy)

#----------------------------------------------------------------------------
# 14 . Calculate Testing Accuracy
#----------------------------------------------------------------------------
print(border)
print("14 . Calculate Testing Accuracy")
print(border)

Y_test_pred = model.predict(X_test_scaled)

test_accuracy = accuracy_score(Y_test, Y_test_pred)

print("Testing Accuracy :", test_accuracy)

print("Classification Report :")
print(classification_report(Y_test, Y_test_pred, zero_division=0))

#----------------------------------------------------------------------------
# 15 . Generate Confusion Matrix
#----------------------------------------------------------------------------
print(border)
print("15 . Generate Confusion Matrix")
print(border)

cm = confusion_matrix(Y_test, Y_test_pred, labels=[0, 1])

print("Confusion Matrix :")
print(cm)

plt.figure(figsize=(6, 5))
plt.imshow(cm, interpolation="nearest", cmap="Blues")
plt.title("Employee Attrition Confusion Matrix")
plt.colorbar()

plt.xticks([0, 1], ["Stay (0)", "Leave (1)"])
plt.yticks([0, 1], ["Stay (0)", "Leave (1)"])

plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------
# 16 . Plot Loss Curve
#----------------------------------------------------------------------------
print(border)
print("16 . Plot Loss Curve")
print(border)

plt.figure(figsize=(8, 5))

plt.plot(model.loss_curve_, color="blue", label="Training Loss")

plt.title("MLP Model Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------
# 17 . Create PredictAttrition() Function
#----------------------------------------------------------------------------
print(border)
print("17 . Create PredictAttrition() Function")
print(border)

def PredictAttrition(employee_data):

    columns = [
        "Age",
        "MonthlyIncome",
        "YearsAtCompany",
        "TotalWorkingYears",
        "DistanceFromHome",
        "JobSatisfaction",
        "WorkLifeBalance",
        "OverTime",
        "NumCompaniesWorked",
        "TrainingTimesLastYear"
    ]

    employee_df = pd.DataFrame(employee_data, columns=columns)

    employee_df["OverTime"] = employee_df["OverTime"].replace({
        "Yes": 1,
        "No": 0
    })

    employee_scaled = scalar.transform(employee_df)

    prediction = model.predict(employee_scaled)
    probability = model.predict_proba(employee_scaled)

    return prediction, probability

print("PredictAttrition() function created successfully")

#----------------------------------------------------------------------------
# 18 . Test Five New Employee Records
#----------------------------------------------------------------------------
print(border)
print("18 . Test Five New Employee Records")
print(border)

new_employees = [
    [25, 2500, 1, 3, 20, 2, 2, "Yes", 3, 1],
    [45, 8500, 15, 22, 5, 4, 3, "No", 1, 3],
    [30, 4000, 3, 7, 15, 1, 1, "Yes", 4, 2],
    [38, 6500, 10, 15, 8, 3, 4, "No", 2, 4],
    [28, 3200, 2, 5, 25, 2, 2, "Yes", 3, 1]
]

predictions, probabilities = PredictAttrition(new_employees)

for i in range(len(new_employees)):

    print("Employee :", i + 1)
    print("Employee Data :", new_employees[i])
    print("Prediction Probability :", probabilities[i])

    if predictions[i] == 1:
        print("Prediction : Employee is likely to leave")
    else:
        print("Prediction : Employee is likely to stay")

    print("-" * 50)

#----------------------------------------------------------------------------
# 19 . Explain Overfitting and Underfitting
#----------------------------------------------------------------------------
print(border)
print("19 . Explain Overfitting and Underfitting")
print(border)

difference = train_accuracy - test_accuracy

print("Training Accuracy :", train_accuracy)
print("Testing Accuracy :", test_accuracy)
print("Accuracy Difference :", difference)

if train_accuracy < 0.70 and test_accuracy < 0.70:
    print("Model may be suffering from Underfitting")
elif difference > 0.10:
    print("Model may be suffering from Overfitting")
else:
    print("No strong indication of overfitting based on accuracy difference")

print("Note : This is a basic check. Accuracy alone cannot confirm overfitting.")

#----------------------------------------------------------------------------
# End of Employee Attrition Prediction System
#----------------------------------------------------------------------------