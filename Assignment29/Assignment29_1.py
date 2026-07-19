# Q1) Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not.

import os
import sys

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule


class IsFileExists:

    def __init__(self):
        self.Filename = ""
    
    def Accept(self):
        self.FileName = input("Enter the file name to check exists or not : ")
    
    def CheckFileExists(self):
        isFileExists = False
        for FolderName,SubFolder,FilesName in os.walk(os.path.dirname(__file__)):
            for fName in FilesName:
                if (fName == self.FileName):
                    isFileExists = True

        
        if (isFileExists == True):
            print(f"{self.FileName} is Exists")
        else:
            print(f"{self.FileName} is Not Exists")


def main():
    fObj = IsFileExists()

    fObj.Accept()

    fObj.CheckFileExists()


if __name__ == "__main__":
    main()
