import os 
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

border = "-"*65
def GetData():
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    DataPath = parent_directory +"\\MarvellousAdvertising.csv"
    # Step 1 : Load the data
    print(border)
    print("Step 1 : Load the data")
    print(border)

    df = pd.read_csv(DataPath)

    return df

def CleanDataset(df):
    #step 2 : Remove unwanted column
    print(border)
    print("Step 2 : Remove unwanted column")
    print(border)

    if "Unnamed: 0" in df.columns:
        df = df.drop(columns=["Unnamed: 0"])
    
    return df

def CheckMissingValues(df):
    print(border)
    print("Step 3 : Check missing values")
    print(border)

    print("Total missing values : ")
    print(border)
    print(df.isnull().sum())
    print(border)

    return df

def StatisticalSummary(df):
    # Step 4 : Statistical Summary
    print(border)
    print("Step 4 : Statistical Summary")
    print(border)

    print(df.describe())

def Correlation(df):
    # Step 5 : Correlation
    print(border)
    print(" Step 5 : Correlation")
    print(border)

    print(df.corr())

def SeparateIndependentDependentVariables(df):
    # Step 6 : Separate Independent and Dependent variables
    print(border)
    print("Step 6 : Split Independent and Dependent variables")
    print(border)

    X = df[["TV","radio","newspaper"]]
    Y = df["sales"]

    print("Independent variables : ")
    print(X.head())

    print("Dependent variables : ")
    print(Y.head())

    return X,Y,df 

def SplitDataset(X,Y):
    # Step 7 : Split the dataset
    print(border)
    print("Step 7 : Split the dataset")
    print(border)

    X_train,X_test,Y_train,Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42
    )

    print("Training Data : ",X_train.shape)
    print("Testing Data : ",X_test.shape)

    return X_train,X_test,Y_train,Y_test

def CreateAndTrainModel(X_train,Y_train):
    # Step 8 : Create and train the model
    print(border)
    print("Step 8 : Create and train the model")
    print(border)

    model = LinearRegression()

    model = model.fit(X_train,Y_train)
    
    print("Model trained successfully")

    return model

def TestTheModel(model,X_test,Y_test):
    # Step 9 : Test the model
    print(border)
    print("Step 9 : Test the model")
    print(border)

    Y_pred = model.predict(X_test)

    print("Expected answers : ")
    print(Y_test)
    print("Predicted answers : ",)
    print(Y_pred)

def main():
    df = GetData()
    df = CleanDataset(df)
    df = CheckMissingValues(df)
    StatisticalSummary(df)
    Correlation(df)
    X,Y,df = SeparateIndependentDependentVariables(df)
    X_train,X_test,Y_train,Y_test = SplitDataset(X,Y)
    model = CreateAndTrainModel(X_train,Y_train)
    TestTheModel(model,X_test,Y_test)



if __name__ == "__main__":
    main()