import os
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# ---------------------------------------------------------
# Step 1: Get Data
# ---------------------------------------------------------

def GetData():
    parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
    DataPath = parent_directory +"\\MarvellousInfosystems_PlayPredictor.csv"
    data = pd.read_csv(DataPath)

    print("Dataset:")
    print(data)

    return data


# ---------------------------------------------------------
# Step 2: Clean, Prepare and Manipulate Data
# ---------------------------------------------------------

def PrepareData(data):

    weather_encoder = LabelEncoder()
    temperature_encoder = LabelEncoder()
    play_encoder = LabelEncoder()

    data["Wether"] = weather_encoder.fit_transform(
        data["Wether"]
    )

    data["Temperature"] = temperature_encoder.fit_transform(
        data["Temperature"]
    )

    data["Play"] = play_encoder.fit_transform(
        data["Play"]
    )

    print("\nDataset after Label Encoding:")
    print(data)

    return (
        data,
        weather_encoder,
        temperature_encoder,
        play_encoder
    )


# ---------------------------------------------------------
# Step 3: Train Data
# ---------------------------------------------------------

def TrainData(data):

    X = data[["Wether", "Temperature"]]
    Y = data["Play"]

    K = 3

    model = KNeighborsClassifier(
        n_neighbors=K
    )

    model.fit(X, Y)

    return model


# ---------------------------------------------------------
# Step 4: Test Data
# ---------------------------------------------------------

def TestData(
    model,
    weather_encoder,
    temperature_encoder,
    play_encoder
):

    weather = input("Enter Weather: ")
    temperature = input("Enter Temperature: ")

    weather_value = weather_encoder.transform(
        [weather]
    )[0]

    temperature_value = temperature_encoder.transform(
        [temperature]
    )[0]

    # Create DataFrame with the same feature names
    test_data = pd.DataFrame(
        [[weather_value, temperature_value]],
        columns=["Wether", "Temperature"]
    )

    prediction = model.predict(test_data)

    result = play_encoder.inverse_transform(
        prediction
    )

    print("\nPrediction:", result[0])


# ---------------------------------------------------------
# Step 5: Calculate Accuracy
# ---------------------------------------------------------

def CheckAccuracy(data):

    X = data[["Wether", "Temperature"]]
    Y = data["Play"]

    # Divide into two equal parts
    X_train, X_test, Y_train, Y_test = train_test_split(
        X,
        Y,
        test_size=0.5,
        random_state=42,
        stratify=Y
    )

    print("\nTraining Data:")
    print(Y_train.value_counts())

    print("\nTesting Data:")
    print(Y_test.value_counts())

    print("\nAccuracy for different values of K:")

    for K in range(1, 6):

        model = KNeighborsClassifier(
            n_neighbors=K
        )

        model.fit(X_train, Y_train)

        Y_predicted = model.predict(X_test)

        accuracy = accuracy_score(
            Y_test,
            Y_predicted
        )

        print(
            "K =", K,
            "Accuracy =", accuracy * 100,
            "%"
        )


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

def main():

    # Step 1
    data = GetData()

    # Step 2
    (
        data,
        weather_encoder,
        temperature_encoder,
        play_encoder
    ) = PrepareData(data)

    # Step 3
    model = TrainData(data)

    print("\nModel trained successfully.")

    # Step 4
    TestData(
        model,
        weather_encoder,
        temperature_encoder,
        play_encoder
    )

    # Step 5
    CheckAccuracy(data)


if __name__ == "__main__":
    main()