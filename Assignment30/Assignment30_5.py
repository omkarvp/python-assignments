# 5: Schedule a task that executes every five minutes.
# The task should write the current date and time into a file named:
# Marvellous.txt
# New entries should be appended without removing previous entries.
# Example file contents:
# Task executed at: 25-07-2026 04:30:00 PM
# Task executed at: 25-07-2026 04:35:00 PM
# Task executed at: 25-07-2026 04:40:00 PM



import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class TaskToExecuteAndLog:

    def __init__(self,LogFileName):
        self.LogFileName = LogFileName

    def LogDateTime(self):
        Border = "-"*65

        currentDirectory = os.path.dirname(os.path.abspath(__file__))
        FilePath = currentDirectory+"\\"+ self.LogFileName

        currentDate = datetime.datetime.now()
        currentDate = currentDate.strftime("%d-%m-%Y %I:%M:%S %p")
        LogStatement = "Task executed at: " + currentDate

        if(os.path.isfile(FilePath)): 
            fObj = open(self.LogFileName,"a")
            fObj.write(LogStatement + "\n")
        else:
            fObj = open(self.LogFileName,"w")

            fObj.write(Border + "\n")
            fObj.write("Marvellous Automation Script \n")
            fObj.write(Border + "\n\n")
            fObj.write(LogStatement + "\n")


    def ScheduleToLog(self):
        schedule.every(5).minutes.do(self.LogDateTime)

        while True:
            schedule.run_pending()
            time.sleep(1)
            
def main():
    DisplayModule()

    cObj = TaskToExecuteAndLog("Marvellous.txt")
    
    cObj.ScheduleToLog()


if __name__ == "__main__":
    main()

    