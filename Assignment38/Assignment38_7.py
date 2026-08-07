# 7. Create a scatter plot of:
# StudyHours vs PreviousScore
# Use different colors for Pass and Fail students.


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

#scatter plot
plt.figure(figsize=(7,5))

colors = {0: "red", 1: "green"}
labels = {0: "Fail", 1: "Pass"}

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["StudyHours"],temp["PreviousScore"],color=colors[sp],label = labels[sp])

plt.title("StudyHours vs PreviousScore")

plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")

plt.legend()
plt.grid()
plt.show()