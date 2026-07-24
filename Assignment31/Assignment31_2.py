# 2: Create a function named:
# DisplayMessage(message)
# Schedule the function using:
# schedule.every(5).seconds.do(DisplayMessage, message)
# The message should be accepted from the user.


import os
import sys
import schedule
import time

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule
def DisplayMessage(message):
    print(message)
        
    
def main():
    DisplayModule()

    Message = input("Enter message : ")

    schedule.every(5).seconds.do(DisplayMessage, Message)

    while True:
        schedule.run_pending()
        time.sleep(1)




if __name__ == "__main__":
    main()