import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    precision_score,
    recall_score,
    f1_score
)

border = "-" * 75

#----------------------------------------------------------------------------
# 1 . Load and Understand the Dataset
#----------------------------------------------------------------------------
print(border)
print("1 . Load and Understand the Dataset")
print(border)

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
DataPath = parent_directory +"\\Loan_Default.csv"

data = pd.read_csv(DataPath)

print("Complete Dataset :")
print(data)

print("First 5 Records :")
print(data.head())

print("Dataset Shape :", data.shape)
print("Column Names :", data.columns)

#----------------------------------------------------------------------------
# 2 . Exploratory Data Analysis (EDA)
#----------------------------------------------------------------------------
print(border)
print("2 . Exploratory Data Analysis (EDA)")
print(border)

print("Statistical Summary :")
print(data.describe())

print("Data Types :")
print(data.dtypes)

print("Unique Values :")
print(data.nunique())

#----------------------------------------------------------------------------
# 3 . Find Missing Values
#----------------------------------------------------------------------------
print(border)
print("3 . Find Missing Values")
print(border)

print(data.isnull().sum())

for column in data.columns:
    if data[column].isnull().any():
        if data[column].dtype == "object":
            data[column] = data[column].fillna(data[column].mode()[0])
        else:
            data[column] = data[column].fillna(data[column].median())

print("Missing Values After Handling :")
print(data.isnull().sum())

#----------------------------------------------------------------------------
# 4 . Check Whether Target Classes Are Balanced
#----------------------------------------------------------------------------
print(border)
print("4 . Check Target Class Balance")
print(border)

print("Default Class Count :")
print(data["Default"].value_counts())

print("Default Class Percentage :")
print(data["Default"].value_counts(normalize=True) * 100)

data["Default"].value_counts().sort_index().plot(
    kind="bar",
    color=["green", "red"]
)

plt.title("Loan Default Class Distribution")
plt.xlabel("Default (0 = Low Risk, 1 = High Risk)")
plt.ylabel("Number of Applicants")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------
# 5 . Encode Categorical Variables
#----------------------------------------------------------------------------
print(border)
print("5 . Encode Categorical Variables")
print(border)

data["PreviousDefault"] = data["PreviousDefault"].map({
    "No": 0,
    "Yes": 1
})

data["HomeOwnership"] = data["HomeOwnership"].map({
    "Rent": 0,
    "Own": 1,
    "Mortgage": 2
})

print("Categorical Variables Encoded Successfully")
print(data.head())

#----------------------------------------------------------------------------
# 6 . Separate Independent and Dependent Variables
#----------------------------------------------------------------------------
print(border)
print("6 . Separate Independent and Dependent Variables")
print(border)

X = data[
    [
        "Age",
        "Income",
        "LoanAmount",
        "CreditScore",
        "EmploymentYears",
        "ExistingLoans",
        "MonthlyDebt",
        "LoanTerm",
        "PreviousDefault",
        "HomeOwnership"
    ]
]

Y = data["Default"].astype(int)

print("Independent Variables :")
print(X.head())

print("Dependent Variable :")
print(Y.head())

#----------------------------------------------------------------------------
# 7 . Train Test Split
#----------------------------------------------------------------------------
print(border)
print("7 . Train Test Split")
print(border)

#----------------------------------------------------------------------------
# 8 . Stratified Splitting
#----------------------------------------------------------------------------
print(border)
print("8 . Stratified Splitting")
print(border)

# Stratify preserves the approximate class proportions in both sets.
# It is useful when default and non-default classes are imbalanced.

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

print("Training Class Distribution :")
print(Y_train.value_counts(normalize=True))

print("Testing Class Distribution :")
print(Y_test.value_counts(normalize=True))

#----------------------------------------------------------------------------
# 9 . Scale the Features (Standard Scalar)
#----------------------------------------------------------------------------
print(border)
print("9 . Scale the Features (Standard Scalar)")
print(border)

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

print("Scaled Training Data :")
print(X_train_scaled[:5])

#----------------------------------------------------------------------------
# 10 . Create MLPClassifier
#----------------------------------------------------------------------------
print(border)
print("10 . Create MLPClassifier")
print(border)

model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)

print(model)

#----------------------------------------------------------------------------
# 11 . Train the Model
#----------------------------------------------------------------------------
print(border)
print("11 . Train the Model")
print(border)

model.fit(X_train_scaled, Y_train)

print("Model Trained Successfully")

#----------------------------------------------------------------------------
# 12 . Calculate Accuracy
#----------------------------------------------------------------------------
print(border)
print("12 . Calculate Accuracy")
print(border)

Y_train_pred = model.predict(X_train_scaled)
Y_test_pred = model.predict(X_test_scaled)

train_accuracy = accuracy_score(Y_train, Y_train_pred)
test_accuracy = accuracy_score(Y_test, Y_test_pred)

print("Number of Iterations :", model.n_iter_)
print("Training Accuracy :", train_accuracy)
print("Testing Accuracy :", test_accuracy)

#----------------------------------------------------------------------------
# 13 . Generate Confusion Matrix
#----------------------------------------------------------------------------
print(border)
print("13 . Generate Confusion Matrix")
print(border)

cm = confusion_matrix(Y_test, Y_test_pred, labels=[0, 1])

print("Confusion Matrix :")
print(cm)

plt.figure(figsize=(6, 5))
plt.imshow(cm, interpolation="nearest", cmap="Blues")
plt.title("Loan Default Confusion Matrix")
plt.colorbar()

plt.xticks([0, 1], ["Low Risk (0)", "High Risk (1)"])
plt.yticks([0, 1], ["Low Risk (0)", "High Risk (1)"])

plt.xlabel("Predicted Label")
plt.ylabel("Actual Label")

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------
# 14 . Generate Classification Report
#----------------------------------------------------------------------------
print(border)
print("14 . Generate Classification Report")
print(border)

print(classification_report(
    Y_test,
    Y_test_pred,
    labels=[0, 1],
    target_names=["Low Default Risk", "High Default Risk"],
    zero_division=0
))

#----------------------------------------------------------------------------
# 15 . Calculate Precision, Recall and F1-Score
#----------------------------------------------------------------------------
print(border)
print("15 . Calculate Precision, Recall and F1-Score")
print(border)

precision = precision_score(Y_test, Y_test_pred, zero_division=0)
recall = recall_score(Y_test, Y_test_pred, zero_division=0)
f1 = f1_score(Y_test, Y_test_pred, zero_division=0)

print("Precision :", precision)
print("Recall :", recall)
print("F1-Score :", f1)

#----------------------------------------------------------------------------
# 16 . Plot Training Loss
#----------------------------------------------------------------------------
print(border)
print("16 . Plot Training Loss")
print(border)

plt.figure(figsize=(8, 5))
plt.plot(model.loss_curve_, color="blue", label="Training Loss")

plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------
# 17 . Test the Model on New Loan Applicants
#----------------------------------------------------------------------------
print(border)
print("17 . Test New Loan Applicants")
print(border)

def PredictLoanDefault(applicant_data):

    columns = [
        "Age",
        "Income",
        "LoanAmount",
        "CreditScore",
        "EmploymentYears",
        "ExistingLoans",
        "MonthlyDebt",
        "LoanTerm",
        "PreviousDefault",
        "HomeOwnership"
    ]

    applicant_df = pd.DataFrame(applicant_data, columns=columns)

    applicant_df["PreviousDefault"] = applicant_df["PreviousDefault"].replace({
        "Yes": 1,
        "No": 0
    })

    applicant_df["HomeOwnership"] = applicant_df["HomeOwnership"].replace({
        "Rent": 0,
        "Own": 1,
        "Mortgage": 2
    })

    applicant_scaled = scalar.transform(applicant_df)

    prediction = model.predict(applicant_scaled)
    probability = model.predict_proba(applicant_scaled)

    for i in range(len(prediction)):

        print("Applicant :", i + 1)
        print("Applicant Data :", applicant_df.iloc[i].to_dict())
        print("Prediction Probability :", probability[i])

        if prediction[i] == 1:
            print("Prediction : High Default Risk")
        else:
            print("Prediction : Low Default Risk")

        print("-" * 50)

    return prediction

new_applicants = [
    [25, 30000, 15000, 580, 2, 3, 900, 36, "Yes", "Rent"],
    [45, 90000, 20000, 780, 15, 1, 400, 24, "No", "Own"],
    [35, 50000, 25000, 650, 7, 2, 700, 48, "No", "Mortgage"],
    [29, 40000, 30000, 600, 3, 4, 1200, 60, "Yes", "Rent"],
    [50, 100000, 15000, 800, 20, 1, 300, 36, "No", "Own"]
]

predictions = PredictLoanDefault(new_applicants)

#----------------------------------------------------------------------------
# Hyperparameter Experiment
# Experiment 1 - Activation Function
#----------------------------------------------------------------------------
print(border)
print("18 . Experiment 1 - Activation Function")
print(border)

activation_results = []

for activation_name in ["identity", "logistic", "tanh", "relu"]:

    experiment_model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation=activation_name,
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    experiment_model.fit(X_train_scaled, Y_train)

    experiment_prediction = experiment_model.predict(X_test_scaled)

    experiment_accuracy = accuracy_score(Y_test, experiment_prediction)

    activation_results.append([
        activation_name,
        experiment_accuracy,
        experiment_model.n_iter_
    ])

    print("Activation :", activation_name)
    print("Testing Accuracy :", experiment_accuracy)
    print("Iterations :", experiment_model.n_iter_)
    print("-" * 50)

activation_df = pd.DataFrame(
    activation_results,
    columns=["Activation", "Testing Accuracy", "Iterations"]
)

print("Activation Experiment Results :")
print(activation_df)

#----------------------------------------------------------------------------
# Experiment 2 - Hidden Layers
#----------------------------------------------------------------------------
print(border)
print("19 . Experiment 2 - Hidden Layers")
print(border)

hidden_layer_results = []

for hidden_layers in [(10,), (20, 10), (50, 25), (100, 50, 25)]:

    experiment_model = MLPClassifier(
        hidden_layer_sizes=hidden_layers,
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    experiment_model.fit(X_train_scaled, Y_train)

    experiment_prediction = experiment_model.predict(X_test_scaled)

    experiment_accuracy = accuracy_score(Y_test, experiment_prediction)

    hidden_layer_results.append([
        str(hidden_layers),
        experiment_accuracy,
        experiment_model.n_iter_
    ])

    print("Hidden Layers :", hidden_layers)
    print("Testing Accuracy :", experiment_accuracy)
    print("Iterations :", experiment_model.n_iter_)
    print("-" * 50)

hidden_layer_df = pd.DataFrame(
    hidden_layer_results,
    columns=["Hidden Layers", "Testing Accuracy", "Iterations"]
)

print("Hidden Layer Experiment Results :")
print(hidden_layer_df)

#----------------------------------------------------------------------------
# Experiment 3 - Learning Rate
#----------------------------------------------------------------------------
print(border)
print("20 . Experiment 3 - Learning Rate")
print(border)

learning_rate_results = []

for learning_rate in [0.001, 0.01, 0.1]:

    experiment_model = MLPClassifier(
        hidden_layer_sizes=(32, 16),
        activation="relu",
        solver="adam",
        learning_rate_init=learning_rate,
        max_iter=1000,
        random_state=42
    )

    experiment_model.fit(X_train_scaled, Y_train)

    experiment_prediction = experiment_model.predict(X_test_scaled)

    experiment_accuracy = accuracy_score(Y_test, experiment_prediction)

    learning_rate_results.append([
        learning_rate,
        experiment_accuracy,
        experiment_model.n_iter_
    ])

    print("Learning Rate :", learning_rate)
    print("Testing Accuracy :", experiment_accuracy)
    print("Iterations :", experiment_model.n_iter_)
    print("-" * 50)

learning_rate_df = pd.DataFrame(
    learning_rate_results,
    columns=["Learning Rate", "Testing Accuracy", "Iterations"]
)

print("Learning Rate Experiment Results :")
print(learning_rate_df)

#----------------------------------------------------------------------------
# Save the Model
#----------------------------------------------------------------------------
print(border)
print("Save the Model")
print(border)

joblib.dump(model, "loan_default_model.pkl")
joblib.dump(scalar, "loan_default_scalar.pkl")

print("Model and Scalar saved successfully")

#----------------------------------------------------------------------------
# End of Loan Default Prediction System
#----------------------------------------------------------------------------
