# Design machine learning application which follows below steps as
# •	Step 1:
# Get Data
# •	Step 2:
# Clean, Prepare and Manipulate data
# •	Step 3:
# Train Data
# •	Step 4:
# Test Data
# •	Step 5:
# Calculate Accuracy

import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler


border = "-"*40

class MarvellousClassifier:

    def __init__(self,DataPath):
        self.DataPath = DataPath

    
    # Step 1 : Load the dataset from CSV file
    def LoadDataset(self,DataPath):
        print(border)
        print("Step 1 : Load the dataset from CSV file")
        print(border)

        df = pd.read_csv(self.DataPath)

        return df

    #step 2 : Clean the Dataset
    def CleanDataset(self,df):
        print(border)
        print("Step 2 : Clean the Dataset")
        print(border)

        df.dropna(inplace=True)

        print("Shape of Dataset : ",df.shape)
        print("Total records : ",df.shape[0])
        print("Total columns : ",df.shape[1])

        return df

    #step 3 : Separate Independent and Dependent Variables
    def SeparateVariables(self,df):
        print(border)
        print("step 3 : Separate Independent and Dependent Variables")
        print(border)

        X = df.drop(columns=['Class'])
        Y = df['Class']

        print("Shape of X : ",X.shape)
        print("Shape of Y : ",Y.shape)
        print(border)
        print("Input columns : ",X.columns.tolist())
        print("Output columns : Class")
        print(border)

        return X,Y

    #step 4 : Split the dataset into training and testing
    def SplitDataForTrainTest(self,X,Y):
        print(border)
        print("step 4 : Split the dataset into training and testing")
        print(border)

        X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.5,random_state=42,stratify=Y)

        print(border)
        print("Details of training and testing data")
        print("Shape of X_train : ",X_train.shape)
        print("Shape of X_test : ",X_test.shape)
        print("Shape of Y_train : ",Y_train.shape)
        print("Shape of Y_test : ",Y_test.shape)

        return X_train, X_test, Y_train, Y_test

    #step 5 : Feature scaling
    def FeatureScaling(self,X_train,X_test):
        print(border)
        print("step 5 : Feature scaling")
        print(border)

        scalar = StandardScaler()
        X_train_scaled = scalar.fit_transform(X_train)
        X_test_scaled = scalar.fit_transform(X_test)

        print("Feature scaling done")
        print(border)

        return X_train_scaled, X_test_scaled

    #step 6 : Build the model
    def BuildTheModel(self):
        print(border)
        print("step 6 : Build the model")
        print(border)

        model = KNeighborsClassifier(n_neighbors=9)

        print("Classification model is created")

        return model

    #step 7 : Train the model
    def TrainTheModel(self,model,X_train_scaled,Y_train):
        print(border)
        print("step 7 : Train the model")
        print(border)

        model = model.fit(X_train_scaled,Y_train)

        print("Model training completed")
        print(border)
        return model

    #step 8 : Test the model
    def TestTheModel(self,model,X_test_scaled,Y_test):
        print(border)
        print("step 8 : Test the model")
        print(border)

        Y_pred = model.predict(X_test_scaled)

        accuracy = accuracy_score(Y_test,Y_pred)
        print("Model accuracy is : ",accuracy * 100)
        print("Model training completed")

        print(border)
    

def main():
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    DataPath = parent_directory +"\\WinePredictor.csv"
    print(DataPath)
    cObj = MarvellousClassifier(DataPath)
    
    df = cObj.LoadDataset(cObj.DataPath)

    df = cObj.CleanDataset(df)

    X,Y = cObj.SeparateVariables(df)

    X_train, X_test, Y_train, Y_test = cObj.SplitDataForTrainTest(X,Y)

    X_train_scaled, X_test_scaled = cObj.FeatureScaling(X_train,X_test)

    model = cObj.BuildTheModel()

    model = cObj.TrainTheModel(model,X_train_scaled,Y_train)

    cObj.TestTheModel(model,X_test_scaled,Y_test)


if __name__ == "__main__":
    main()