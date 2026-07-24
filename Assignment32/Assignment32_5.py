# 5: Write a program that deletes all empty files from a specified directory every hour.
# The program should:
# •	Scan the directory recursively 
# •	Detect files whose size is zero bytes 
# •	Delete the empty files 
# •	Store deleted file paths in a log file 
# •	Handle permission errors 
# Note: Test the program only on a sample directory.

import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule
Border = "-"*65
def DeleteEmptyFiles(SourceFolderPath):
    LogFileName = 'DeletedLogFile.txt'
    for FolderName,SubFolderName,FileName in os.walk(SourceFolderPath):
        for fName in FileName:
         
            if(os.path.getsize(os.path.join(SourceFolderPath,fName)) == 0):

                fObj = open(LogFileName,"a")

                try:
                    os.remove(os.path.join(SourceFolderPath,fName))
                    fObj.write(f"{Border}\n")
                    fObj.write(f"Deleted File Path : {os.path.join(SourceFolderPath,fName)}\n")
                    fObj.write(f"Date and Time: {datetime.datetime.now()}\n")
                    fObj.write(f"{Border}\n")

                except Exception as eObj:
                    fObj.write(f"Can not Deleted File Path : {os.path.join(SourceFolderPath,fName)} : {eObj}")
                    continue

                fObj.close()

def main():
    if(len(sys.argv) == 2):
        SourceFolderName = sys.argv[1]
        
        if(os.path.isabs(SourceFolderName)):
            SourceFolderPath = SourceFolderName
        else:
            SourceFolderPath = os.path.abspath(SourceFolderName)

        if(os.path.isdir(SourceFolderPath)):
            schedule.every(10).seconds.do(DeleteEmptyFiles,SourceFolderPath)

            while True:
                schedule.run_pending()
                time.sleep(1)

        else:
            print(f"Not a directory : {SourceFolderPath}")
    else:
        print("Invalid provided argument")

if __name__ == "__main__":
    main()