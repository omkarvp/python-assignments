# 2: Write a Python program that monitors the size of a specified file every 30 seconds.
# Write the following details into:
# FileSizeLog.txt
# •	File path 
# •	File size in bytes 
# •	Date and time 
# Handle the situation where the file does not exist.


import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule
Border = "-"*65
def MonitorFileSize(FilePath):

    timeStamp = datetime.datetime.now()

    if(os.path.exists("FileSizeLog.txt")):
        fObj = open("FileSizeLog.txt","a")
    else:
        fObj = open("FileSizeLog.txt","w")

    fObj.write(f"{Border}\n")
    fObj.write(f"Marvellous Automations Script\n")
    fObj.write(f"{Border}\n")
    fObj.write(f"Filename : {FilePath}\n")
    fObj.write(f"File size in bytes : {os.path.getsize(FilePath)}\n")
    fObj.write(f"Creation time : {timeStamp.strftime("%I:%M:%S %p")}\n")
    fObj.write(f"{Border}\n")

    fObj.close()

def main():
    DisplayModule()  
    if(len(sys.argv) == 2):

        FileName = sys.argv[1]

        if(os.path.isabs(FileName)):
            FilePath = FileName
        else:
            FilePath = os.path.abspath(FileName)

        if(os.path.exists(FilePath) and os.path.isfile(FilePath)):
            schedule.every(5).seconds.do(MonitorFileSize,FilePath)
            
            while True:
                schedule.run_pending()
                time.sleep(1)

        else:
            print("File does not exists")

    

if __name__ == "__main__":
    main()