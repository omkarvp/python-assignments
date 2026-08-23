# 4.	Write a Python program to calculate the Euclidean distance between two points before and after applying feature scaling, and explain the difference in results.
import numpy as np
from sklearn.preprocessing import StandardScaler

border = "-" * 65


# Step 1
# ---------------------------------------------------
# Function Name : LoadData
# Description : Load two points
# Input : None
# Output : Two points
# ---------------------------------------------------

def LoadData():

    Point1 = [25, 20000]
    Point2 = [35, 80000]

    print("Point 1 : ", Point1)
    print("Point 2 : ", Point2)

    return Point1, Point2


# Step 2
# ---------------------------------------------------
# Function Name : CalculateDistance
# Description : Calculate Euclidean distance
# Input : Two points
# Output : Distance
# ---------------------------------------------------

def CalculateDistance(Point1, Point2):

    Distance = np.sqrt(
        (Point1[0] - Point2[0]) ** 2 +
        (Point1[1] - Point2[1]) ** 2
    )

    return Distance


# Step 3
# ---------------------------------------------------
# Function Name : ScaleData
# Description : Scale the points using StandardScaler
# Input : Two points
# Output : Scaled points
# ---------------------------------------------------

def ScaleData(Point1, Point2):

    Data = [
        Point1,
        Point2
    ]

    scaler = StandardScaler()

    ScaledData = scaler.fit_transform(Data)

    return ScaledData


def main():

    Point1, Point2 = LoadData()

    # Distance before scaling
    DistanceBefore = CalculateDistance(
        Point1,
        Point2
    )

    print("Distance before scaling : ", DistanceBefore)

    # Scaling
    ScaledData = ScaleData(
        Point1,
        Point2
    )

    # Distance after scaling
    DistanceAfter = CalculateDistance(
        ScaledData[0],
        ScaledData[1]
    )

    print("Distance after scaling : ", DistanceAfter)


if __name__ == "__main__":
    main()
