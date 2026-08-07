# 4. Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.
import os
import pandas as pd

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

Border = "*"*65

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath)

##################################################
# Use value_counts() to analyze the distribution of FinalResult.
##################################################

print(Border)
print("Use value_counts() to analyze the distribution of FinalResult")
print(Border+"\n")

ValuesCount = df["FinalResult"].value_counts()
print(ValuesCount)

##################################################
# Calculate the percentage of Pass and Fail students.
##################################################

print(Border)
print("Calculate the percentage of Pass and Fail students")
print(Border+"\n")

PercentageOfPassAndFailed = df["FinalResult"].value_counts(normalize=True)*100
print(f"The percentage of Pass students : {PercentageOfPassAndFailed[1]} %")
print(f"The percentage of Fail students : {PercentageOfPassAndFailed[0]} %")
