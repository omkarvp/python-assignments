# 8.	Using the regression model created in the previous question, write a Python program to predict marks for 6 study hours and display the predicted value. 

from sklearn.linear_model import LinearRegression

def MarvellousPredictor():

    # Load the data
    X = [
        [1, 7],
        [2, 6],
        [3, 7],
        [4, 6],
        [5, 8]
    ]

    Y = [50, 55, 60, 65, 70]

    # Create and train the regression model
    model = LinearRegression()
    model.fit(X, Y)

    # Print coefficients
    print("Coefficient for StudyHours : ", model.coef_[0])
    print("Coefficient for SleepHours : ", model.coef_[1])

    # Print intercept
    print("Intercept : ", model.intercept_)


def main():
    MarvellousPredictor()


if __name__ == "__main__":
    main()
