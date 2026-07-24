# 1: Write a Python program that prints:
# Jay Ganesh...
# every two seconds.
# Use:
# schedule.every(2).seconds.do(...)
# Expected output:
# Jay Ganesh...
# Jay Ganesh...
# Jay Ganesh...


import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class PrintOutput:

    def __init__(self,Statement):
        self.message = Statement

    def Display(self):
        print(datetime.datetime.now())
        print(self.message)

    def ScheduleToDisplay(self):
        schedule.every(2).seconds.do(self.Display)

        while True:
            schedule.run_pending()
            time.sleep(1)
            
def main():
    DisplayModule()

    cObj = PrintOutput("Jay Ganesh...")

    cObj.ScheduleToDisplay()


if __name__ == "__main__":
    main()

    