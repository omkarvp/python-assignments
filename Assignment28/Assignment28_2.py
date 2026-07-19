# Q2) Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.
# ________________________________________
import os
import sys

# Get the parent directory
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add it to Python's search path
sys.path.insert(0, parent_dir)

from Assignments_Module import DisplayModule

class CountWordsInFile:
    def __init__(self):
        self.WordsInFile = 0
        self.FileName = ""

    
    def Accept(self):
       self.FileName = input("Enter the file name : ")

    def CountLinesUsingUserDefinedFunction(self):
        try:
            fObj = open(self.FileName,"r")
            Data = fObj.readlines()
            
            for Words in Data:
                splittedString = len(Words.split())
            
                self.WordsInFile += splittedString
                    
        except FileNotFoundError as FNFE:
            print(FNFE)
        except Exception as eobj:
            print("Exception occured :",eobj)
    
    def CountLinesUsingInBuiltFunctionSplit(self):
        try:
            fObj = open(self.FileName,"r")
            Data = fObj.read()
            self.WordsInFile = len(Data.split())
                    
        except FileNotFoundError as FNFE:
            print(FNFE)
        except Exception as eobj:
            print("Exception occured :",eobj)

def main():
    DisplayModule()
    
    print("")

    cObj = CountWordsInFile()

    cObj.Accept()

    cObj.CountLinesUsingUserDefinedFunction()

    if cObj.WordsInFile > 0:
        print(f"Total number of lines Using UserDefined function in file : '{cObj.FileName}' is : {cObj.WordsInFile}")

    
    cObj.CountLinesUsingInBuiltFunctionSplit()

    if cObj.WordsInFile > 0:
        print(f"Total number of lines Using In-Built Function in file : '{cObj.FileName}' is : {cObj.WordsInFile}")


if __name__ == "__main__":
    main()