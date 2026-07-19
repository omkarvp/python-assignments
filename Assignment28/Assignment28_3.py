# Q3) Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the screen.
# Input:
# Demo.txt
# Expected Output:
# Display each line of Demo.txt one by one.

import os
import sys

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
# print(parent_directory)

sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class DisplayContentOfFileLineByLine:

    def __init__(self):
        self.FileName = ""
        self.ContentOfFile = ""

    def Accept(self):
        self.FileName = input("Enter the File name : ")

    def DisplayContents(self):
        fObj = open(self.FileName,"r")
        Data = fObj.read()
        print(f"The contents of the file {self.FileName} is : \n")
        print(Data)

    def displayFileLineByLine(self):

        try:
            # Open the file safely
            with open(self.FileName, 'r') as file:
                # Loop through the file object directly (memory efficient)
                for line_number,line in enumerate(file, 1):
                    
                    # end='' prevents adding extra blank lines, as lines already contain '\n'
                    print(f"Line {line_number}: {line}", end='')
                print() # Print a final newline for clean formatting
                
        except FileNotFoundError:
            print(f"Error: The file '{self.FileName}' does not exist.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")



def main():
    DisplayModule()
    print("")

    cObj = DisplayContentOfFileLineByLine()

    cObj.Accept()

    cObj.DisplayContents()

    print("")
    cObj.displayFileLineByLine()
    
if __name__ == "__main__":
    main()