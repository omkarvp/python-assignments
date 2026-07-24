# 4: Write a program that creates a new log file after every ten minutes.
# The filename should contain the current date and time.
# Example:
# MarvellousLog_25_07_2026_16_30_00.txt
# Log file created successfully.
# Creation Time: 25-07-2026 04:30:00 PM

import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule
Border = "-"*50
def CreateLogFile():
    timestamp = datetime.datetime.now()
    formattedTimestamp = timestamp.strftime("%d_%m_%Y_%H_%M_%S")
    LogFileName = "MarvellousLog_%s.txt"%formattedTimestamp

    fObj = open(LogFileName,'w')
    fObj.write(Border+"\n")
    fObj.write("Marvellous Automation Script\n")
    fObj.write(Border+"\n")
    fObj.write("Log file created successfully.\n")
    fObj.write(f"Creation Time : {timestamp.strftime("%d-%m-%Y %H:%M:%S %p")}")
    fObj.write("\n"+Border)
    fObj.close()

def main():
    DisplayModule()

    schedule.every(10).minutes.do(CreateLogFile)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()