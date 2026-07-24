# 6: Write a program that schedules the following messages:
# •	Monday at 9:00 AM: Start your weekly goals 
# •	Wednesday at 5:00 PM: Review your weekly progress 
# •	Friday at 6:00 PM: Weekly work completed 
# Use:
# schedule.every().monday.at(...)
# schedule.every().wednesday.at(...)
# schedule.every().friday.at(...)


import os
import sys
import schedule
import time

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule


def ScheduleMonday():
    print("Start your weekly goals")
    
def ScheduleWednesday():
    print("Review your weekly progress")

def ScheduleFriday():
    print("Weekly work completed")
    

def main():
    DisplayModule()

    schedule.every().monday.at("09:00").do(ScheduleMonday)
    schedule.every().wednesday.at("17:00").do(ScheduleWednesday)
    schedule.every().friday.at("18:00").do(ScheduleFriday)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()