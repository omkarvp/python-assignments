# 9. Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.


import os
import pandas as pd
import matplotlib.pyplot as plt

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

Border = "*"*65

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath)

###########################################################################
# A plot showing relationship between AssignmentsCompleted and FinalResult.
###########################################################################

print(Border)
print("A plot showing relationship between AssignmentsCompleted and FinalResult : ")
print(Border+"\n")

#box plot
plt.figure(figsize=(7,5))

colors = {0: "red", 1: "green"}
labels = {0: "Fail", 1: "Pass"}

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["AssignmentsCompleted"],
                temp["FinalResult"],
                color=colors[sp],
                label=labels[sp],
                s=70)

plt.title("AssignmentsCompleted vs FinalResult")
plt.xlabel("AssignmentsCompleted")
plt.ylabel("FinalResult")
plt.yticks([0,1],["Fail","Pass"])
plt.legend()
plt.grid(True)
plt.show()
