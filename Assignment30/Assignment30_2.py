# 2: Write a Python program that displays the current date and time after every one minute.
# Use the datetime module.
# Expected output:
# Current Date and Time: 25-07-2026 04:30:00 PM



import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class CurrentDateAndTime:

    def Display(self):
        currentDate = datetime.datetime.now()
        currentDate = currentDate.strftime("%d-%m-%Y %I:%M:%S %p")
        print("Current Date and Time: ",currentDate)

    def ScheduleToDisplayDateAndTime(self):
        schedule.every().minute.do(self.Display)

        while True:
            schedule.run_pending()
            time.sleep(1)
            
def main():
    DisplayModule()

    cObj = CurrentDateAndTime()

    cObj.ScheduleToDisplayDateAndTime()


if __name__ == "__main__":
    main()

    