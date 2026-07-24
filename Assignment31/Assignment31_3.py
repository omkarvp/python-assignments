# 3: Write a program that scans a specified directory every minute.
# The task should display:
# •	Directory name 
# •	Number of files 
# •	Number of subdirectories 
# •	Date and time of scanning 
# Use the os module.
# Example output:
# Directory Scanned: E:/Data
# Total Files: 15
# Total Subdirectories: 4
# Scan Time: 25-07-2026 04:30:00 PM

#commnad line input : python Assignment31_3.py C:\Users\admin\Desktop\Python\Automations\
import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule
def DirectoryScanner(DirectoryPath):
    TotalFiles = 0
    TotalSubdirectories = 0

    for FolderName, SubFolderName, FileName in os.walk(DirectoryPath):
        for fName in FileName:
            if(os.path.isfile(os.path.join(FolderName,fName))):
                TotalFiles +=1

        for SubFolder in SubFolderName:
            if(os.path.isdir(os.path.join(FolderName,SubFolder))):
                TotalSubdirectories +=1

    print(f"Directory Scanned : {DirectoryPath}")
    print(f"Total Files : {TotalFiles}")
    print(f"Total Subdirectories : {TotalSubdirectories}")
    print(f"Scan Time : {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}")
    print("-"*40)

def main():
    DisplayModule()

    if(len(sys.argv) == 2):
        DirectoryPath = sys.argv[1]
        
        schedule.every().minute.do(DirectoryScanner,DirectoryPath)

        while True:
            schedule.run_pending()
            time.sleep(1)


if __name__ == "__main__":
    main()