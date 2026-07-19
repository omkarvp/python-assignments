# Q5) Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in the file or not.
# Input:
# Demo.txt  Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.


import os
import sys

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
# print(parent_directory)

sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class WordInFile:

    def __init__(self):
        self.FileName = ""
        self.Word = ""
        
    def Accept(self):
        try :
            self.FileName = input("Enter the File name : ")
            self.WordToSearch = input("Enter the word to search in the file : ")

        except Exception as eObj:
            print("Default exception occurred : ",eObj)

    def SearchWordInFile(self):
        try: 
            Flag = False
            fReadObj = open(self.FileName,"r")

            Data = fReadObj.read()
            listData = Data.split()

            for word in listData:
                if word == self.WordToSearch:
                    Flag = True
                
            
            if Flag == True:
                print(f"The word {self.WordToSearch} is found in {self.FileName}")
            else:
                print(f"The word {self.WordToSearch} is not found in {self.FileName}")
            
            
        
        except Exception as eObj:
            print("Default exception occurred : ",eObj)

def main():
    DisplayModule()
    print("")

    cObj = WordInFile()

    cObj.Accept()

    cObj.SearchWordInFile() 

    
if __name__ == "__main__":
    main()