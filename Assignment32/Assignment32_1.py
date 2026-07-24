# 1: Write a program that creates a new text file every minute.
# The filename should contain the current timestamp.
# Example:
# File_25_07_2026_16_30_00.txt
# Write the following information into the file:
# •	Filename 
# •	Creation date 
# •	Creation time 

import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

def CreateNewFile():
    timeStamp = datetime.datetime.now()
    FTimeStamp = timeStamp.strftime("%d_%m_%Y_%H_%M_%S")
    FileName = "File_%s.txt"%FTimeStamp

    fObj = open(FileName,"w")

    fObj.write(f"Filename : {FileName}\n")
    fObj.write(f"Creation date : {timeStamp.strftime("%d-%m-%Y")}\n")
    fObj.write(f"Creation time : {timeStamp.strftime("%I:%M:%S %p")}\n")

    fObj.close()

def main():
    DisplayModule()    

    schedule.every().minute.do(CreateNewFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()