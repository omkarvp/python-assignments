import os
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,precision_score
from sklearn.metrics import recall_score,f1_score,confusion_matrix

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import VotingClassifier

border = "-"*65

##########################################################
# Step 1 : Load the dataset
##########################################################
parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
DataPath = parent_directory +"\\Fraudulent_Transaction_Detection.csv"

print(border)
print("Step 1 : Load the dataset")
print(border)

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

X = df.drop("Fraud",axis=1)

Y = df["Fraud"]

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
    random_state=42,
    stratify=Y
)

##########################################################
# Step 5 : Encode categorical features and scale features
##########################################################

print(border)
print("Step 5 : Encode categorical features and scale features")
print(border)

X_train = pd.get_dummies(X_train)
X_test = pd.get_dummies(X_test)

X_train, X_test = X_train.align(
    X_test,
    join='left',
    axis=1,
    fill_value=0
)

scalar = StandardScaler()

X_train = scalar.fit_transform(X_train)
X_test = scalar.transform(X_test)

##########################################################
# Step 6 : Create the Individual models
##########################################################

print(border)
print("Step 6 : Create the Individual models")
print(border)

model_det = DecisionTreeClassifier(random_state=42)

model_bag = BaggingClassifier(
    estimator=DecisionTreeClassifier(random_state=42),
    n_estimators=10,
    random_state=42
)

model_rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model_ada = AdaBoostClassifier(
    n_estimators=50,
    random_state=42
)

##########################################################
# Step 7 : Create the Voting Classifier
##########################################################

print(border)
print("Step 7 : Create the Voting Classifier")
print(border)

model_voting = VotingClassifier(
    estimators=[
        ('decision_tree',
         DecisionTreeClassifier(random_state=42)),
        ('random_forest',
         RandomForestClassifier(n_estimators=100,random_state=42)),
        ('adaboost',
         AdaBoostClassifier(n_estimators=50,random_state=42))
    ],
    voting='soft'
)

##########################################################
# Step 8 : Train the models
##########################################################

print(border)
print("Step 8 : Train the models")
print(border)

model_det.fit(X_train,Y_train)

model_bag.fit(X_train,Y_train)

model_rf.fit(X_train,Y_train)

model_ada.fit(X_train,Y_train)

model_voting.fit(X_train,Y_train)

##########################################################
# Step 9 : Test the models
##########################################################

print(border)
print("Step 9 : Test the models")
print(border)

Y_pred_det = model_det.predict(X_test)

Y_pred_bag = model_bag.predict(X_test)

Y_pred_rf = model_rf.predict(X_test)

Y_pred_ada = model_ada.predict(X_test)

Y_pred_voting = model_voting.predict(X_test)

##########################################################
# Step 10 : Evaluate the models
##########################################################

print(border)
print("Step 10 : Evaluate the models")
print(border)

models = {
    "Decision Tree" : Y_pred_det,
    "Bagging" : Y_pred_bag,
    "Random Forest" : Y_pred_rf,
    "AdaBoost" : Y_pred_ada,
    "Voting" : Y_pred_voting
}

results = []

for name,Y_pred in models.items():

    acc = accuracy_score(Y_test,Y_pred)

    pre = precision_score(
        Y_test,Y_pred,zero_division=0
    )

    rec = recall_score(
        Y_test,Y_pred,zero_division=0
    )

    f1 = f1_score(
        Y_test,Y_pred,zero_division=0
    )

    print()
    print(border)
    print(name)
    print(border)

    print("Accuracy : ",acc)
    print("Precision : ",pre)
    print("Recall : ",rec)
    print("F1 Score : ",f1)

    print("Confusion Matrix : ")
    print(confusion_matrix(Y_test,Y_pred))

    results.append({
        "Algorithm" : name,
        "Accuracy" : acc,
        "Precision" : pre,
        "Recall" : rec,
        "F1" : f1
    })

##########################################################
# Step 11 : Final comparison
##########################################################

print(border)
print("Step 11 : Final comparison")
print(border)

result = pd.DataFrame(results)

print(result.to_string(index=False))

##########################################################
# Step 12 : Recommend the best model
##########################################################

print(border)
print("Step 12 : Recommend the best model")
print(border)

best_model = result.loc[
    result["F1"].idxmax()
]

print("Recommended Algorithm : ",
      best_model["Algorithm"])

print("Best F1 Score : ",
      best_model["F1"])