# 9.	Write a Python program using scikit-learn to generate a classification report for the following data:
# actual   = [1,1,1,1,0,0,0,0]
# predicted = [1,1,0,1,0,1,0,0]
# Display the complete classification report including precision, recall, F1-score, and support.

from sklearn.metrics import classification_report

border = "-" * 65


# Step 1
# ---------------------------------------------------
# Function Name : LoadData
# Description : Load actual and predicted values
# Input : None
# Output : Actual and Predicted values
# ---------------------------------------------------

def LoadData():

    actual = [1, 1, 1, 1, 0, 0, 0, 0]

    predicted = [1, 1, 0, 1, 0, 1, 0, 0]

    print("Actual values : ", actual)
    print("Predicted values : ", predicted)

    return actual, predicted


# Step 2
# ---------------------------------------------------
# Function Name : GenerateReport
# Description : Generate classification report
# Input : Actual and Predicted values
# Output : Classification report
# ---------------------------------------------------

def GenerateReport(actual, predicted):

    Report = classification_report(
        actual,
        predicted
    )

    print("Classification Report : ")
    print(Report)


def main():

    actual, predicted = LoadData()

    GenerateReport(
        actual,
        predicted
    )


if __name__ == "__main__":
    main()
