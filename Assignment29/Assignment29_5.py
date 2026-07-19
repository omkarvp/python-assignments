# Q5) Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of occurrences) of that string in the file.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.



import os
import sys

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class AcceptInputFromCMDandCompareTwoFiles:

    def __init__(self):
        self.FileName = ""
        self.StringToSearch = ""
    
    def Accept(self):
        try :
            self.FileName = input("Enter the File name : ")
            self.StringToSearch = input("Enter the word to search in the file : ")

        except Exception as eObj:
            print("Default exception occurred : ",eObj)
            
    
    def DisplayContents(self):
        try:
            count = 0
            with open(self.FileName,"r") as file:
                for line in file:
                    count += line.count(self.StringToSearch)
            
            print(f"The string '{self.StringToSearch}' appears {count} times in '{self.FileName}'.")

        except Exception as eObj:
            print("Default exception occured : ",eObj)

        
def main():
    fObj = AcceptInputFromCMDandCompareTwoFiles()

    fObj.Accept()

    fObj.DisplayContents()


if __name__ == "__main__":
    main()
