# 4: Create a task that executes every day at 9:00 AM and prints:
# Namskar...
# Use:
# schedule.every().day.at("09:00").do(...)




import os
import sys
import schedule
import time

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class TaskToExecuteEveryDay:

    def __init__(self,Statement):
        self.Statement = Statement

    def Display(self):
        print(self.Statement)

    def ScheduleToPrintEveryDay(self):
        schedule.every().day.at("09:00").do(self.Display)

        while True:
            schedule.run_pending()
            time.sleep(1)
            
def main():
    DisplayModule()

    cObj = TaskToExecuteEveryDay("Namskar...")

    cObj.ScheduleToPrintEveryDay()


if __name__ == "__main__":
    main()

    