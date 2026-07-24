# 1: Write a program that accepts:
# •	A message from the user 
# •	A time interval in seconds 
# Schedule the program to display the message repeatedly after the specified interval.
# Example input:
# Enter message: Jay Ganesh
# Enter interval in seconds: 5
# Expected output:
# Jay Ganesh
# every five seconds.
# Validate that the interval is greater than zero.

import os
import sys
import schedule
import time

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class DisplayRepeatedly:

    def __init__(self):
        self.Message = ""
        self.TimeInterval = 0

    def Accept(self):
        self.Message = input("Enter message : ")
        self.TimeInterval = int(input("Enter interval in seconds : "))

    def ValidateInterval(self):
        if(self.TimeInterval <= 0):
            return False

        return True

    def DisplayMessage(self):
        print(self.Message)

    def ScheduleToDisplayRepeatedly(self):
        schedule.every(self.TimeInterval).seconds.do(self.DisplayMessage)

        while True:
            schedule.run_pending()
            time.sleep(1)

    
def main():
    DisplayModule()

    cObj = DisplayRepeatedly()

    cObj.Accept()

    Ret = cObj.ValidateInterval()

    if(Ret == True):
        cObj.ScheduleToDisplayRepeatedly()
    else:
        print("The interval should be greater than zero")




if __name__ == "__main__":
    main()