# 5: Write a program that accepts a directory name from the user and counts the number of files inside it every five minutes.
# Write the result into:
# DirectoryCountLog.txt
# Each entry should contain:
# •	Directory path 
# •	Number of files 
# •	Date and time 


import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

Border = "-"*65

def CountFilesAndLog(DirectoryPath):
    
    TotalFiles = 0
    
    for FolderName, SubFolderName, FileName in os.walk(DirectoryPath):
        for fName in FileName:
            if(os.path.isfile(os.path.join(FolderName,fName))):
                TotalFiles +=1

    if(os.path.exists(os.path.abspath(os.path.dirname('DirectoryCountLog.txt')))):
       fObj = open("DirectoryCountLog.txt","a")
    else:
       fObj = open("DirectoryCountLog.txt","w")

    fObj.write(Border+"\n")
    fObj.write("Marvellouse Automation Script \n")
    fObj.write(Border+"\n")
    fObj.write(f"Total Files : {DirectoryPath} \n")
    fObj.write(f"Number of files : {TotalFiles} \n")
    fObj.write(f"Date and time : {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")} \n")
    fObj.write(Border+"\n\n")

def main():
    DisplayModule()

    DirectoryName = input("Enter directory name : ")
    if(os.path.isabs(DirectoryName)):
        AbsolutePath = DirectoryName
    else:
        AbsolutePath = os.path.abspath(os.path.dirname(DirectoryName))
    
    if(os.path.isdir(AbsolutePath)):
        schedule.every(5).seconds.do(CountFilesAndLog,AbsolutePath)

        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("This is not a directory")
if __name__ == "__main__":
    main()