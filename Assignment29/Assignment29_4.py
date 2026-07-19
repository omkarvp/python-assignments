# Q4) Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of both files.
# •	If both files contain the same contents, display Success 
# •	Otherwise display Failure 
# ________________________________________
# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure


import os
import sys

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class AcceptInputFromCMDandCompareTwoFiles:

    def __init__(self):
        self.FirstFileName = ""
        self.SecondFileName = ""
    
    def Accept(self):
        try:
            self.FirstFileName = sys.argv[1]
            self.SecondFileName = sys.argv[2]

        except IndexError as iObj:
            print("Please enter the file name")
        
        except Exception as eObj:
            print("Default exception occured : ",eObj)
            
    
    def DisplayContents(self):
        try:
            FlagMatched = True
            with open(self.FirstFileName,"r") as firstFile, open(self.SecondFileName,"r") as secondFile:
                # FirstFileData = firstFile.read()
                SecondFileData = secondFile.readlines()
                
                for line_number, line in enumerate(firstFile,1):
                    if (line != SecondFileData[line_number-1]):
                        FlagMatched = False
                        break
                    
                if(FlagMatched == True):
                    print("Success")
                else:
                    print("Failure")

        except Exception as eObj:
            print("Default exception occured : ",eObj)

        
def main():
    fObj = AcceptInputFromCMDandCompareTwoFiles()

    fObj.Accept()

    fObj.DisplayContents()


if __name__ == "__main__":
    main()
