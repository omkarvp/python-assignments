# 6: Write a script that schedules the following tasks:
# •	Print Lunch Time! every day at 1:00 PM. 
# •	Print Wrap up work every day at 6:00 PM. 
# Both tasks should be handled by separate functions.




import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class TimeTable:
    LunchTimeStr = "13:00"
    LogoutTimeStr = "18:00"

    def DisplayAlarm(self):
        currentHourAndMin = datetime.datetime.now().strftime("%H:%M")
        print("currentHourAndMin : ",currentHourAndMin)
        if(currentHourAndMin == self.LunchTimeStr):
            print("Lunch Time!")
        elif(currentHourAndMin == self.LogoutTimeStr):
            print("Wrap up work")

    def ScheduleLunchTime(self):

        schedule.every().day.at(TimeTable.LunchTimeStr).minutes.do(self.DisplayAlarm)

        while True:
            schedule.run_pending()
            time.sleep(1)

    def ScheduleLogoutTime(self):
        
        schedule.every().day.at(TimeTable.LogoutTimeStr).minutes.do(self.DisplayAlarm)

        while True:
            schedule.run_pending()
            time.sleep(1)
            
def main():
    DisplayModule()

    cObj = TimeTable()
    
    cObj.ScheduleLunchTime()

    cObj.ScheduleLogoutTime()


if __name__ == "__main__":
    main()

    