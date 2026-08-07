# 8. Draw a boxplot for Attendance.
# Identify if any outliers are present.


import os
import pandas as pd
import matplotlib.pyplot as plt

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

Border = "*"*65

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath)

##################################################
# Scatter plot of
# StudyHours vs PreviousScore
##################################################

print(Border)
print("Scatter plot of : ")
print("StudyHours vs PreviousScore : ")
print(Border+"\n")

#box plot
plt.figure(figsize=(7,5))

plt.boxplot(df["Attendance"])

plt.title("StudyHours vs PreviousScore")

plt.ylabel("Attendance")

plt.legend()
plt.grid()
plt.show()

Q1 = df["Attendance"].quantile(0.25)
Q3 = df["Attendance"].quantile(0.75)

IQR = Q3 - Q1

outliers = df[(df["Attendance"] < Q1 - 1.5*IQR) |
              (df["Attendance"] > Q3 + 1.5*IQR)]

print(outliers)