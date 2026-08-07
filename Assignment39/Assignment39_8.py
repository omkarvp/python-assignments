import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report
)


Border = "-"*65
#########################################
# Step - 1 : Load the Dataset
#########################################


print(Border)
print("Step - 1 : Load the Dataset")
print(Border)

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath) # df stands for Data Frame

print("Data set loaded successfully")

#############################################
# Step - 2 : Exploaratory Data Analysis (EDA)
#############################################

print(Border)
print("Step - 2 : Exploaratory Data Analysis (EDA)")
print(Border)

print("Shape of dataset : ",df.shape)

print("Column names : ",list(df.columns))

print("Missing values per column : ")

print(df.isnull().sum()) #canonical function call

print("Class distribution (FinalResult count) : ")

print(df["FinalResult"].value_counts())

print("Statistical report of Dataser : ")

print(df.describe())

########################################################
# Step - 3 : Decide Indenpendent and Dependent Varibles
########################################################

print(Border)
print("Step - 3 : Decide Indenpendent and Dependent Varibles")
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

print("X Shape : ",X.shape)
print("Y Shape : ",Y.shape)

########################################################
# Step - 4 : Visualization of dataset
########################################################

print(Border)
print("Step - 4 : Visualization of dataset")
print(Border)

#scatter plot
plt.figure(figsize=(7,5))

colors = {0: "red", 1: "green"}
labels = {0: "Fail", 1: "Pass"}

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["StudyHours"],temp["Attendance"],color=colors[sp],label = labels[sp])

plt.title("StudyHours vs Attendance")

plt.xlabel("StudyHours")
plt.ylabel("Attendance")

plt.legend()
plt.grid()
plt.show()

########################################################
# Step - 5 : Split the dataset for training and testing
########################################################

print(Border)
print("Step - 5 : Split the dataset for training and testing")
print(Border)

X_train , X_test, Y_train, Y_test = train_test_split(X,Y,test_size = 0.5, random_state = 42)

print("Dataset spliting activity done")

print("X : ",X.shape) # (30,4)
print("Y : ",Y.shape) # (30,)

print("X_Train : ",X_train.shape) #(15 , 4)
print("X_test : ",X_test.shape) #(15 , 4)

print("Y_Train : ",Y_train.shape) #(15 , )
print("Y_test : ",Y_test.shape) #(15 , )


########################################################
# Step - 6 : Build the model
########################################################

print(Border)
print("Step - 6 : Build the model")
print(Border)

model = DecisionTreeClassifier(max_depth=5)

print("Model gets created successfully")


########################################################
# Step - 7 : Train the model
########################################################

print(Border)
print("Step - 7 : Train the model")
print(Border)

model.fit(X_train,Y_train)

print("Model trained successfully")


########################################################
# Step - 8 : Evaluate/Test the model
########################################################

print(Border)
print("Step - 8 : Evaluate/Test the model")
print(Border)

Y_pred = model.predict(X_test)

print("Model testing done")

print("Expected answers : ")
print(X_test)
print("Predicted answers : ")
print(Y_pred)


########################################################
# Step - 9 : Evaluate the modele performance
########################################################

print(Border)
print("Step - 9 : Evaluate the modele performance")
print(Border)

accuracy = accuracy_score(Y_test,Y_pred)

print("Accuracy of model is : ",accuracy * 100)
print("Confusion matrix is : ")
cm= confusion_matrix(Y_test, Y_pred)
print(cm)

print("Classification report : ",accuracy * 100)
print(classification_report(Y_test,Y_pred))