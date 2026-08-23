import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    precision_score,
    recall_score,
    f1_score
)


# Step - 1
# ---------------------------------------------------
# Function Name : LoadData
# Descriptiom : Load and explore the Breast Cancer dataset
# Input : None
# Output : Data frame
# Author : Omkar Vishnu Pataskar
# Date : 16-Aug-2026
# ----------------------------------------------------

def LoadData():

    data = load_breast_cancer()

    df = pd.DataFrame(
        data.data,
        columns=data.feature_names
    )

    df["target"] = data.target

    print("Dataset loaded successfully")

    print("Number of Records : ", df.shape[0])
    print("Number of Features : ", df.shape[1] - 1)

    print("\nFirst 5 records : ")
    print(df.head())

    print("\nTarget Names : ")
    print(data.target_names)

    print("\nTarget Distribution : ")
    print(df["target"].value_counts())

    return df


# Step - 2
# ---------------------------------------------------
# Function Name : PreprocessData
# Descriptiom : It performs data preprocessing and EDA
# Input : Data Frame
# Output : Updated Data frame
# Author : Omkar Vishnu Pataskar
# Date : 16-Aug-2026
# ----------------------------------------------------

def PreprocessData(df):

    # Check missing values
    print("\nMissing values : ")
    print(df.isnull().sum())

    # Handle missing values
    df = df.fillna(df.median())

    print("\nMissing values handled successfully")

    # Summary statistics
    print("\nSummary Statistics : ")
    print(df.describe())

    # Feature correlation
    plt.figure(figsize=(15, 12))

    correlation = df.drop("target", axis=1).corr()

    sns.heatmap(
        correlation,
        cmap="coolwarm",
        linewidths=0.5
    )

    plt.title("Feature Correlation Matrix")
    plt.show()

    print("Data preprocessing and EDA completed")

    return df


# Step - 3
# ---------------------------------------------------
# Function Name : SplitData
# Descriptiom : It performs splitting activity
# Input : Data Frame
# Output : 4 Subset for training and testing
# Author : Omkar Vishnu Pataskar
# Date : 16-Aug-2026
# ----------------------------------------------------

def SplitData(df):

    X = df.drop("target", axis=1)
    Y = df["target"]

    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42,
        stratify=Y
    )

    print("Dataset splitting completed successfully")

    print("Training Data : ", X_train.shape)
    print("Testing Data : ", X_test.shape)

    return X_train, X_test, Y_train, Y_test


# Step - 4 : Scale the data and train the model
# ---------------------------------------------------
# Function Name : TrainModel
# Descriptiom : It performs feature scaling and model training
# Input : Training features and labels
# Output : Trained model and scaler
# Author : Omkar Vishnu Pataskar
# Date : 16-Aug-2026
# ----------------------------------------------------

def TrainModel(X_train, Y_train):

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)

    model = LogisticRegression(max_iter=10000)

    model = model.fit(X_train_scaled, Y_train)

    print("Feature scaling completed")
    print("Model trained successfully")

    return model, scaler


# Step - 5 : Evaluate the model
# ---------------------------------------------------
# Function Name : EvaluateModel
# Descriptiom : It performs model testing and evaluation
# Input : model, scaler, testing data(features, labels)
# Output : None
# Author : Omkar Vishnu Pataskar
# Date : 16-Aug-2026
# ----------------------------------------------------

def EvaluateModel(model, scaler, X_test, Y_test):

    X_test_scaled = scaler.transform(X_test)

    Y_pred = model.predict(X_test_scaled)

    # Accuracy
    Accuracy = accuracy_score(Y_test, Y_pred)

    print(f"\nAccuracy is : {Accuracy*100:.2f}%", )

    # Confusion Matrix
    CM = confusion_matrix(Y_test, Y_pred)

    print("\nConfusion Matrix : ")
    print(CM)

    # Precision
    Precision = precision_score(Y_test, Y_pred)

    print("\nPrecision is : ", Precision)

    # Recall
    Recall = recall_score(Y_test, Y_pred)

    print("Recall is : ", Recall)

    # F1-Score
    F1 = f1_score(Y_test, Y_pred)

    print("F1-Score is : ", F1)

    # Confusion Matrix Visualization
    plt.figure(figsize=(6, 5))

    sns.heatmap(
        CM,
        annot=True,
        fmt="d",
        cmap="Blues",
        xticklabels=["Malignant", "Benign"],
        yticklabels=["Malignant", "Benign"]
    )

    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")

    plt.show()


# ----------------------------------------------------
# Function Name : main
# Descriptiom : Entry point function
# Input : None
# Output : None
# Author : Omkar Vishnu Pataskar
# Date : 16-Aug-2026
# ----------------------------------------------------

def main():

    # Step - 1
    df = LoadData()

    # Step - 2
    df = PreprocessData(df)

    # Step - 3
    X_train, X_test, Y_train, Y_test = SplitData(df)

    # Step - 4
    model, scaler = TrainModel(X_train, Y_train)

    # Step - 5
    EvaluateModel(
        model,
        scaler,
        X_test,
        Y_test
    )


if __name__ == "__main__":
    main()
