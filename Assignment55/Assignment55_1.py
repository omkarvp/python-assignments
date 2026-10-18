import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

from sklearn.ensemble import VotingClassifier

border = "-"*65

##########################################################
# Step 1 : Load the dataset
##########################################################

print(border)
print("Step 1 : Load the dataset")
print(border)

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
DataPath = parent_directory +"\\Customer_Loan_Approval.csv"

df = pd.read_csv(DataPath)

print("Shape of dataset : ",df.shape)
print("First few records : ")
print(df.head())

##########################################################
# Step 2 : Check for missing values
##########################################################

print(border)
print("Step 2 : Check for missing values")
print(border)

print(df.isnull().sum())

df = df.dropna()

##########################################################
# Step 3 : Separate features and labels
##########################################################

print(border)
print("Step 3 : Separate features and labels")
print(border)

X = df.drop("LoanApproved",axis=1)

Y = df["LoanApproved"]

print("X shape : ",X.shape)
print("Y shape : ",Y.shape)

##########################################################
# Step 4 : Split dataset for training and testing
##########################################################

print(border)
print("Step 4 : Split dataset for training and testing")
print(border)

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=42
)

##########################################################
# Step 5 : Scale the features
##########################################################

print(border)
print("Step 5 : Scale the features")
print(border)

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

##########################################################
# Step 6.1 : Create the Individual models
##########################################################

print(border)
print("Step 6.1 : Create the Individual models")
print(border)

model_logi = LogisticRegression(max_iter=1000)

model_det = DecisionTreeClassifier(random_state=42)

model_knn = KNeighborsClassifier(n_neighbors=5)

##########################################################
# Step 6.2 : Train the Individual models
##########################################################

print(border)
print("Step 6.2 : Train the Individual models")
print(border)

model_logi.fit(X_train,Y_train)

model_det.fit(X_train,Y_train)

model_knn.fit(X_train,Y_train)

##########################################################
# Step 7 : Calculate Individual model accuracy
##########################################################

print(border)
print("Step 7 : Calculate Individual model accuracy")
print(border)

Y_pred_logi = model_logi.predict(X_test)
Y_pred_det = model_det.predict(X_test)
Y_pred_knn = model_knn.predict(X_test)

acc_logi = accuracy_score(Y_test,Y_pred_logi)
acc_det = accuracy_score(Y_test,Y_pred_det)
acc_knn = accuracy_score(Y_test,Y_pred_knn)

print("Logistic Regression Accuracy : ",acc_logi)
print("Decision Tree Accuracy : ",acc_det)
print("KNN Accuracy : ",acc_knn)

##########################################################
# Step 8 : Create the Hard Voting Classifier
##########################################################

print(border)
print("Step 8 : Create the Hard Voting Classifier")
print(border)

model_hard = VotingClassifier(
    estimators=[
        ('logistic',LogisticRegression(max_iter=1000)),
        ('decision_tree',DecisionTreeClassifier(random_state=42)),
        ('knn',KNeighborsClassifier(n_neighbors=5))
    ],
    voting='hard'
)

##########################################################
# Step 9 : Train and test the Hard Voting model
##########################################################

print(border)
print("Step 9 : Train and test the Hard Voting model")
print(border)

model_hard.fit(X_train,Y_train)

Y_pred_hard = model_hard.predict(X_test)

acc_hard = accuracy_score(Y_test,Y_pred_hard)

print("Hard Voting Accuracy : ",acc_hard)

##########################################################
# Step 10 : Create the Soft Voting Classifier
##########################################################

print(border)
print("Step 10 : Create the Soft Voting Classifier")
print(border)

model_soft = VotingClassifier(
    estimators=[
        ('logistic',LogisticRegression(max_iter=1000)),
        ('decision_tree',DecisionTreeClassifier(random_state=42)),
        ('knn',KNeighborsClassifier(n_neighbors=5))
    ],
    voting='soft'
)

##########################################################
# Step 11 : Train and test the Soft Voting model
##########################################################

print(border)
print("Step 11 : Train and test the Soft Voting model")
print(border)

model_soft.fit(X_train,Y_train)

Y_pred_soft = model_soft.predict(X_test)

acc_soft = accuracy_score(Y_test,Y_pred_soft)

print("Soft Voting Accuracy : ",acc_soft)

##########################################################
# Step 12 : Compare all model accuracies
##########################################################

print(border)
print("Step 12 : Compare all model accuracies")
print(border)

result = pd.DataFrame({
    "Model" : [
        "Logistic Regression",
        "Decision Tree",
        "KNN",
        "Hard Voting",
        "Soft Voting"
    ],
    "Accuracy" : [
        acc_logi,
        acc_det,
        acc_knn,
        acc_hard,
        acc_soft
    ]
})

print(result)