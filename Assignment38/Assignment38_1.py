# 1. Write a Python program to load the file student_performance_ml.csv using pandas. Display:
# •	First 5 records 
# •	Last 5 records 
# •	Total number of rows and columns 
# •	List of column names 
# •	Data types of each column

import os
import pandas as pd

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

Border = "*"*65

DataPath = parent_directory + "\\student_performance_ml.csv"

df = pd.read_csv(DataPath)

#########################################
# First 5 records
#########################################

print(Border+"\n")
print("First 5 records : \n")
print(Border+"\n")

print(df.head())
print("\n")

#########################################
# Last 5 records
#########################################

print(Border+"\n")
print("Last 5 records : \n")
print(Border+"\n")

print(df.tail())
print("\n")

#########################################
# Total number of rows and columns
#########################################

print(Border+"\n")
print(f"Total number of rows : {df.shape[0]} and columns : {df.shape[1]}\n")
print(Border+"\n")

print("\n")


#########################################
# List of column names
#########################################

print(Border+"\n")
print(f"List of column names : \n")
print(Border+"\n")

print(list(df.columns))
print("\n")

#########################################
# Data types of each column
#########################################

print(Border+"\n")
print(f"Data types of each column : \n")
print(Border+"\n")

print(df.dtypes)
print("\n")


#########################################
# Output
#########################################

# D:\python-assignments\Assignment38>python Assignment38_1.py
# *****************************************************************

# First 5 records :

# *****************************************************************

#    StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  FinalResult
# 0         2.0          65             45                     3           5            0
# 1         3.0          70             50                     4           6            0
# 2         4.0          75             55                     5           6            0
# 3         5.0          80             60                     6           7            1
# 4         6.0          85             65                     7           7            1


# *****************************************************************

# Last 5 records :

# *****************************************************************

#     StudyHours  Attendance  PreviousScore  AssignmentsCompleted  SleepHours  FinalResult
# 25         5.2          81             61                     6           7            1
# 26         6.2          87             66                     7           7            1
# 27         7.2          91             72                     8           8            1
# 28         8.2          96             78                     9           8            1
# 29         1.8          63             44                     2           5            0


# *****************************************************************

# Total number of rows : 30 and columns : 6

# *****************************************************************



# *****************************************************************

# List of column names :

# *****************************************************************

# ['StudyHours', 'Attendance', 'PreviousScore', 'AssignmentsCompleted', 'SleepHours', 'FinalResult']


# *****************************************************************

# Data types of each column :

# *****************************************************************

# StudyHours              float64
# Attendance                int64
# PreviousScore             int64
# AssignmentsCompleted      int64
# SleepHours                int64
# FinalResult               int64
# dtype: object



# D:\python-assignments\Assignment38>