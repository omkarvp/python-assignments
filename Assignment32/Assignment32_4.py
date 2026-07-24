# 4: Write a program that copies all .txt files from one directory to another every ten minutes.
# The program should:
# •	Accept source and destination directories 
# •	Validate both directories
# •	Copy only .txt files 
# •	Maintain a log of copied files 
# •	Avoid terminating if one file cannot be copied 

import os
import sys
import schedule
import time
import shutil
import datetime

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

def CopySourceFilesToDestination(SourceFolderPath,DestinationFolderPath):

    for FolderName,SubFolderName,FileName in os.walk(SourceFolderPath):

        for fName in FileName:
            if(os.path.isfile(os.path.join(FolderName,fName))):

                Name,Extension = os.path.splitext(fName)

                FullFilePath = FolderName+"\\"+fName

                if(Extension.lower() == ".txt"):
                    try:
                        shutil.copy(FullFilePath,DestinationFolderPath)
                        LogFile = "CopyLog.txt"
                        with open(LogFile, "a") as fobj:
                            fobj.write(f"{datetime.datetime.now()} : {fName} copied\n")

                    except Exception as e:
                        print("Cannot copy :", FileName)
                        print(e)

                        continue
                    


def main():
    DisplayModule()  

    if(len(sys.argv) == 3):
        
        SourceFolderName = sys.argv[1]

        if(os.path.isabs(SourceFolderName)):
            SourceFolderPath = SourceFolderName
        else:
            SourceFolderPath = os.path.abspath(SourceFolderName)


        DestinationFolderName = sys.argv[2]

        if(os.path.isabs(DestinationFolderName)):
            DestinationFolderPath = DestinationFolderName
        else:
            DestinationFolderPath = os.path.abspath(DestinationFolderName)

        if(os.path.isdir(SourceFolderPath) and os.path.isdir(DestinationFolderPath)):
            schedule.every(10).minutes.do(CopySourceFilesToDestination,SourceFolderPath,DestinationFolderPath)
            
            while True:
                schedule.run_pending()
                time.sleep(1)
        elif (not os.path.isdir(SourceFolderPath)):
            print(f"Not a directory : {SourceFolderPath}")
        elif (not os.path.isdir(DestinationFolderPath)):
            print(f"Not a directory : {DestinationFolderPath}")
    else:
        print("Invalid provided argument")



    

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