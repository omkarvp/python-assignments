# 7.	Write a Python program using LinearRegression to train a regression model using the dataset below. 

from sklearn.linear_model import LinearRegression

def MarvellousPredictor():

    # Load the data
    X = [[1], [2], [3], [4], [5]]
    Y = [50, 55, 60, 65, 70]

    # Create and train the regression model
    model = LinearRegression()
    model.fit(X, Y)

    # Print coefficient
    print("Coefficient : ", model.coef_[0])

    # Print intercept
    print("Intercept : ", model.intercept_)


def main():
    MarvellousPredictor()


if __name__ == "__main__":
    main()
