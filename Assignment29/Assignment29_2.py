# Q2) Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.


import os
import sys

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule


class DisplayContentsOnConsole:

    def __init__(self):
        self.Filename = ""
    
    def Accept(self):
        self.FileName = input("Enter the file name to display the contents : ")
    
    def DisplayContents(self):
        fReadObj = open(self.FileName,"r")
        Contents = fReadObj.read()
        print(Contents)
        fReadObj.close()

        print("")
        print("Another way to display the content using WITH statement")
        with open(self.FileName,"r") as SourceFile:
            for line in SourceFile:
                print(line)
            print("")

        
def main():
    fObj = DisplayContentsOnConsole()

    fObj.Accept()

    fObj.DisplayContents()


if __name__ == "__main__":
    main()
