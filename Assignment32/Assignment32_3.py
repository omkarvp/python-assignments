# 3: Write a program that reads and displays the contents of a specified text file every minute.
# Handle the following conditions:
# •	File does not exist 
# •	File is empty 
# •	Permission is denied 
# •	File cannot be opened 



import os
import sys
import schedule
import time
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule
Border = "-"*65

def ValidateFile(FilePath):
    if not os.path.exists(FilePath):
        print("File does not exist")
        return False


    if os.path.getsize(FilePath) == 0:
        print("File is empty")
        return False

    try:
        with open(FilePath, "r") as f:
            pass

    except PermissionError:
        print("Permission denied:", FilePath)
        return False

    except OSError:
        print("File cannot be opened:", FilePath)
        return False

    return True


def ReadAndDisplayContentOfFile(FilePath):
    try:
        with open(FilePath,"r") as fObj:
            content = fObj.read()
            print(content)

    except Exception as eObj:
        print("Error occured : ",eObj)

def main():
    DisplayModule()  

    if(len(sys.argv) == 2):

        FileName = sys.argv[1]

        if(os.path.isabs(FileName)):
            FilePath = FileName
        else:
            FilePath = os.path.abspath(FileName)

        Ret = ValidateFile(FilePath)

        if(Ret == True):
            schedule.every(5).seconds.do(ReadAndDisplayContentOfFile,FilePath)
            
            while True:
                schedule.run_pending()
                time.sleep(1)


    

if __name__ == "__main__":
    main()


#Output

# D:\python-assignments\Assignment32>python Assignment32_3.py D:\python-assignments\
# *********************
# ===== Jay Ganesh ====
# *********************
# No such file or directory:  D:\python-assignments\

# D:\python-assignments\Assignment32>python Assignment32_3.py PermissionDenied.txt
# *********************
# ===== Jay Ganesh ====
# *********************
# Permission denied:  D:\python-assignments\Assignment32\PermissionDenied.txt

# D:\python-assignments\Assignment32>python Assignment32_3.py Empty.txt
# *********************
# ===== Jay Ganesh ====
# *********************
# File is empty

# D:\python-assignments\Assignment32>python Assignment32_3.py D:\python-assignments\
# *********************
# ===== Jay Ganesh ====
# *********************
# File cannot be opened: D:\python-assignments\