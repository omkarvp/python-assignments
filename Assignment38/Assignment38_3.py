# 3. Using pandas functions, calculate and display:
# •	Average StudyHours 
# •	Average Attendance 
# •	Maximum PreviousScore 
# •	Minimum SleepHours 


import os
import pandas as pd

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

Border = "*"*65

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath)

##################################################
# Average StudyHours
##################################################

print(Border+"\n")
print("Average StudyHours\n")
print(Border+"\n")

print(df["StudyHours"].mean())
print("\n")

##################################################
# Average Attendance
##################################################

print(Border+"\n")
print("Average Attendance\n")
print(Border+"\n")

print(df["Attendance"].mean())
print("\n")

##################################################
# Maximum PreviousScore
##################################################

print(Border+"\n")
print("Maximum PreviousScore\n")
print(Border+"\n")

print(df["PreviousScore"].max())
print("\n")

##################################################
# Minimum SleepHours
##################################################

print(Border+"\n")
print("Minimum SleepHours\n")
print(Border+"\n")

print(df["SleepHours"].min())
print("\n")