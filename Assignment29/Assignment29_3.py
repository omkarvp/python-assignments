# Q3) Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file named Demo.txt, and copies all contents from the given file into Demo.txt.
# ABC.txt
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import os
import sys

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class AcceptInputFromCMDandCopyContentIntoNewFile:

    def __init__(self):
        self.ExistingFileName = ""
        self.NewFileName = "Demo1.txt"
    
    def Accept(self):
        try:
            self.ExistingFileName = sys.argv[1]

        except IndexError as iObj:
            print("Please enter the file name")
        
        except Exception as eObj:
            print("Default exception occured : ",eObj)
            
    
    def DisplayContents(self):
        try:
            fReadExistingFileObj = open(self.ExistingFileName,"r")
            Data = fReadExistingFileObj.read()

            fWriteNewFileObj = open(self.NewFileName,"w")
            fWriteNewFileObj.write(Data)
            
            fReadExistingFileObj.close()
            fWriteNewFileObj.close()

            fReadNewFileObj = open(self.NewFileName,"r")
            NewContent = fReadNewFileObj.read()
            print(f"Content of file {self.NewFileName} is :")
            print("")
            print(NewContent)
            
        except Exception as eObj:
            print("Default exception occured : ",eObj)

        
def main():
    fObj = AcceptInputFromCMDandCopyContentIntoNewFile()

    fObj.Accept()

    fObj.DisplayContents()


if __name__ == "__main__":
    main()
