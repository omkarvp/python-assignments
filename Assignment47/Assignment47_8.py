# 8.	Using the regression model created in the previous question, write a Python program to predict marks for 6 study hours and display the predicted value. 

from sklearn.linear_model import LinearRegression

def MarvellousPredictor():

    # Load the data
    X = [[1], [2], [3], [4], [5]]
    Y = [50, 55, 60, 65, 70]

    # Create and train the regression model
    model = LinearRegression()
    model.fit(X, Y)

    # Predict marks for 6 study hours
    predicted_marks = model.predict([[6]])

    print("Predicted marks for 6 study hours : ", predicted_marks[0])


def main():
    MarvellousPredictor()


if __name__ == "__main__":
    main()
