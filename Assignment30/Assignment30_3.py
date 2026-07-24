# 3: Write a program that schedules a function to print:
# Coding Kar..!
# every 30 minutes.




import os
import sys
import schedule
import time

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class PrintStatement:

    def __init__(self,Statement):
        self.Statement = Statement

    def Display(self):
        print(self.Statement)

    def ScheduleToPrintStatement(self):
        schedule.every(30).minutes.do(self.Display)

        while True:
            schedule.run_pending()
            time.sleep(1)
            
def main():
    DisplayModule()

    cObj = PrintStatement("Coding Kar..!")

    cObj.ScheduleToPrintStatement()


if __name__ == "__main__":
    main()

    