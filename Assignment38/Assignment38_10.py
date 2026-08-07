# 10. Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.


import os
import pandas as pd
import matplotlib.pyplot as plt

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

Border = "*"*65

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath)

###########################################################################
# A Plot SleepHours against FinalResult.
###########################################################################

print(Border)
print("A Plot SleepHours against FinalResult : ")
print(Border+"\n")

#box plot
plt.figure(figsize=(7,5))

colors = {0: "red", 1: "green"}
labels = {0: "Fail", 1: "Pass"}

for sp in df["FinalResult"].unique():
    temp = df[df["FinalResult"] == sp]
    plt.scatter(temp["SleepHours"],
                temp["FinalResult"],
                color=colors[sp],
                label=labels[sp],
                s=70)

plt.title("Plot SleepHours against FinalResult")
plt.xlabel("SleepHours")
plt.ylabel("FinalResult")
plt.yticks([0,1],["Fail","Pass"])
plt.legend()
plt.grid(True)
plt.show()
