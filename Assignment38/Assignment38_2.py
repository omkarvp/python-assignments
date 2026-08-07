# 2. Write a program to:
# •	Display total number of students in the dataset. 
# •	Count how many students Passed (FinalResult = 1). 
# •	Count how many students Failed (FinalResult = 0). 

import os
import pandas as pd

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

Border = "*"*65

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath)

##################################################
# Display total number of students in the dataset
##################################################

print(Border+"\n")
print(f"Display total number of students in the dataset : {df.shape[0]}\n")
print(Border+"\n")

print("\n")

##################################################
# Count how many students Passed (FinalResult = 1)
##################################################

print(Border+"\n")
print(f"Count how many students Passed (FinalResult = 1) : \n")
print(Border+"\n")

ResultOfStudent = df["FinalResult"].value_counts()
print("FinalResult = 1 : ",ResultOfStudent[1])

print("\n")


##################################################
# Count how many students Failed (FinalResult = 0)
##################################################

print(Border+"\n")
print(f"Count how many students Failed (FinalResult = 0) : \n")
print(Border+"\n")

ResultOfStudent = df["FinalResult"].value_counts()
print("FinalResult = 0 : ",ResultOfStudent[0])

print("\n")