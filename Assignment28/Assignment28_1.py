# Q1) Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo.txt.
# ________________________________________
import os
import sys

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add it to Python's search path
sys.path.insert(0, parent_dir)

from Assignments_Module import DisplayModule

class CountLinesInFile:
    def __init__(self):
        self.LinesInFile = 0
        self.FileName = ""

    
    def Accept(self):
       self.FileName = input("Enter the file name : ")

    def CountLines(self):
        try:
            fObj = open(self.FileName,"r")
            
            self.LinesInFile = len(fObj.readlines())
                    
        except FileNotFoundError as FNFE:
            print(FNFE)
        except Exception as eobj:
            print("Exception occured :",eobj)
    

def main():
    DisplayModule()
    
    print("")

    cObj = CountLinesInFile()

    cObj.Accept()

    cObj.CountLines()

    if cObj.LinesInFile > 0:
        print(f"Total number of lines in {cObj.FileName} is : {cObj.LinesInFile}")


if __name__ == "__main__":
    main()