# 6. Plot a histogram of StudyHours.
# Explain what the distribution tells you.


import os
import pandas as pd
import matplotlib.pyplot as plt

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

Border = "*"*65

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath)

##################################################
# Plot a histogram of StudyHours.
##################################################

print(Border)
print("Plot a histogram of StudyHours : ")
print(Border+"\n")

plt.figure(figsize=(7,5))

for sp in df["FinalResult"].unique():
    temp  = df[df["FinalResult"] == sp]
    plt.hist(temp["StudyHours"],label = sp)

plt.title("Marvellous Student Performance for StudyHours Case study")

plt.xlabel("StudyHours")
plt.ylabel("FinalResult")

plt.legend()
plt.grid()
plt.show()