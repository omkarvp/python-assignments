# 5. Based on the dataset values, analyze whether:
# •	Higher StudyHours increase the chance of passing. 
# •	Higher Attendance improves FinalResult. 
# Write your observations in 4–5 lines.

import os
import pandas as pd

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

Border = "*"*65

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath)

##################################################
# Use value_counts() to analyze the distribution of FinalResult.
##################################################

Result = df.groupby("FinalResult")[["StudyHours", "Attendance"]].mean()

print(Border)
print("Students who Fail (FinalResult = 0):")
print(Border+"\n")
print(f"Average StudyHours : {Result.loc[0,"StudyHours"]: .2f}")
print(f"Average Attendance : {Result.loc[0,"Attendance"] : .2f}%")

print(Border)
print("Students who Pass (FinalResult = 1):")
print(Border+"\n")

print(f"Average StudyHours : {Result.loc[1,"StudyHours"]: .2f}")
print(f"Average Attendance : {Result.loc[1,"Attendance"] : .2f}%")



