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
import hashlib

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

def DeleteEmptyFiles(SourceFolderPath):
    LogFileName = 'DeletedLogFile.txt'
    for FolderName,SubFolderName,FileName in os.walk(SourceFolderPath):
        for fName in FileName:
         
            if(os.path.getsize(os.path.join(SourceFolderPath,fName)) == 0):

                fObj = open(LogFileName,"a")

                try:
                    os.remove(os.path.join(SourceFolderPath,fName))
                    fObj.write(f"Deleted File Path : {os.path.join(SourceFolderPath,fName)}")

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
            DeleteEmptyFiles(SourceFolderPath)
        else:
            print(f"Not a directory : {SourceFolderPath}")
    else:
        print("Invalid provided argument")

if __name__ == "__main__":
    main()