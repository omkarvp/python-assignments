# 3. Consider below task
# 1.	Train linear regression model.
# 2.	Predict salary for 6 years of experience.
# 3.	Plot regression line using matplotlib.
# Dataset
# Experience	Salary
# 1	            20000
# 2	            25000
# 3	            30000
# 4	            35000
# 5	            40000
# Expected Output
# Predicted Salary for 6 Years Experience: ₹45000


import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

border = "-" * 65


# Step 1
# ---------------------------------------------------
# Function Name : LoadData
# Description : Load the salary dataset
# Input : None
# Output : X, Y
# ---------------------------------------------------

def LoadData():

    X = [[1], [2], [3], [4], [5]]
    Y = [20000, 25000, 30000, 35000, 40000]

    return X, Y


# Step 2
# ---------------------------------------------------
# Function Name : TrainModel
# Description : Train the linear regression model
# Input : X, Y
# Output : Trained model
# ---------------------------------------------------

def TrainModel(X, Y):

    model = LinearRegression()

    model = model.fit(X, Y)

    print("Model trained successfully")

    return model


# Step 3
# ---------------------------------------------------
# Function Name : PredictSalary
# Description : Predict salary for 6 years experience
# Input : Trained model
# Output : Predicted salary
# ---------------------------------------------------

def PredictSalary(model):

    predicted_salary = model.predict([[6]])

    print(
        "Predicted Salary for 6 Years Experience : ₹",
        predicted_salary[0]
    )


# Step 4
# ---------------------------------------------------
# Function Name : PlotRegression
# Description : Plot data points and regression line
# Input : X, Y, model
# Output : None
# ---------------------------------------------------

def PlotRegression(X, Y, model):

    Y_pred = model.predict(X)

    plt.scatter(
        X,
        Y,
        color="red",
        label="Data Points"
    )

    plt.plot(
        X,
        Y_pred,
        color="green",
        label="Regression Line"
    )

    plt.xlabel("Experience")
    plt.ylabel("Salary")
    plt.title("Experience vs Salary")

    plt.legend()

    plt.show()


# Main Function
# ---------------------------------------------------

def main():

    X, Y = LoadData()

    model = TrainModel(X, Y)

    PredictSalary(model)

    PlotRegression(X, Y, model)


if __name__ == "__main__":
    main()
