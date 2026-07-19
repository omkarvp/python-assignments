# Q4) Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# •	First file is an existing file 
# •	Second file is a new file 
# Copy all contents from the first file into the second file.
# Input:
# ABC.txt  Demo.txt
# Expected Output:
# Contents of ABC.txt copied into Demo.txt.


import os
import sys

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
# print(parent_directory)

sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class CopyContentsToNewFile:

    def __init__(self):
        self.ExistingFileName = ""
        self.NewFileName = ""
        self.AnotherNewFileName = ""
        self.ContentOfFile = ""
    def Accept(self):
        try :
            self.ExistingFileName = input("Enter the Existing File name : ")
            self.NewFileName = input("Enter the New File name : ")

        except Exception as eObj:
            print("Default exception occurred : ",eObj)

    def CopyContents(self):
        try: 
            fReadObj = open(self.ExistingFileName,"r")

            Data = fReadObj.read()
            
            print(f"The contents of the file {self.ExistingFileName} is : \n")
            
            print(Data)

            fWriteObj = open(self.NewFileName,"w")

            fWriteObj.writelines(Data)
            
            fWriteObj.close()

            fNewReadObj = open(self.NewFileName,"r")
            
            NewData = fNewReadObj.read()
            
            print("")
            
            print(f"The contents of the file {self.NewFileName} is : \n")
            
            print(NewData)
        
        except Exception as eObj:
            print("Default exception occurred : ",eObj)
    
    def UserDefindFunction(self):
        try: 
            self.AnotherNewFileName = input("Enter the Another New File name : ")

            with open(self.ExistingFileName,"r") as source, open(self.AnotherNewFileName,"w") as destination:
                for line in source:
                    destination.write(line)
            
            
            print("The content in the destinantion file is : ")
            fAnotherNewFileObj = open(self.AnotherNewFileName,"r")
            NewAnotherData = fAnotherNewFileObj.read()
            print("")
            print(NewAnotherData)

        except Exception as eObj:
            print("Default exception occurred : ",eObj)


def main():
    DisplayModule()
    print("")

    cObj = CopyContentsToNewFile()

    cObj.Accept()

    cObj.CopyContents() 

    cObj.UserDefindFunction() 
    
if __name__ == "__main__":
    main()