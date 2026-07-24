# 7: Write a Python program that performs a file backup every hour.
# The program should:
# 1.	Accept the source file path. 
# 2.	Accept the destination directory path. 
# 3.	Copy the source file to the destination directory. 
# 4.	Add the current date and time to the backup filename. 
# 5.	Write the backup operation details into: 
# backup_log.txt
# Example backup filename:
# Data_25_07_2026_16_30_00.txt
# Example log entry:
# Backup completed successfully at 25-07-2026 04:30:00 PM

# Input : python Assignment30_7.py Demo.txt Logs

import os
import sys
import schedule
import time
import datetime
import shutil

parent_directory = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
sys.path.insert(0,parent_directory)

from Assignments_Module import DisplayModule

class BackUpFile:
    BackupFileName = "backup_log.txt"
    Border = "-"*65

    def __init__(self):
        self.SourceFilePath = ""
        self.DestinationDirectoryPath = ""

    def Accept(self,Data):
        if(len(Data) != 3):
            print("Invalid number of arguments")
            return
        
        self.SourceFilePath = Data[1] 
        self.DestinationDirectoryPath = Data[2] 
        
    def CheckFileAndDirectoryPath(self):
        Ret = True

        Ret = os.path.exists(self.DestinationDirectoryPath)

        if(Ret == False):
            print("Marvellous Automation Error : There is no such directory with name : ",self.DestinationDirectoryPath)
            return 
        
        Ret = os.path.isdir(self.DestinationDirectoryPath)
        
        if(Ret == False):
            print("Marvellous Automation Error : It is not a directory with name : ",self.DestinationDirectoryPath)
            return

        Ret = os.path.isfile(self.SourceFilePath)

        if(Ret == False):
            print("Marvellous Automation Error : File doesn't exists : ",self.SourceFilePath)
            return

        return True
    
    def BackupFileAndLog(self):
        timeStamp = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S")

        LogFileName = "Data_%s.txt"%timeStamp
        LogFileName = LogFileName.replace(" ","_")
        LogFileName = LogFileName.replace(":","_")

        AbsPathBackupFileName = self.DestinationDirectoryPath+"\\"+LogFileName

        shutil.copyfile(self.SourceFilePath,AbsPathBackupFileName)

        fWriteBackupObj = open(BackUpFile.BackupFileName,"a")

        fWriteBackupObj.write(BackUpFile.Border + "\n")
        fWriteBackupObj.write("Marvellous Automation Script \n")
        fWriteBackupObj.write(BackUpFile.Border + "\n")

        fWriteBackupObj.write(f"\nBackup Filename : {LogFileName}")
        fWriteBackupObj.write(f"\nLog Entry: Backup completed successfully at : {datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")}")

        fWriteBackupObj.write("\n"+BackUpFile.Border + "\n\n")

    def ScheduleToBackupFile(self):
        
        schedule.every(10).seconds.do(self.BackupFileAndLog)

        while True:
            schedule.run_pending()
            time.sleep(1)
            
def main():
    DisplayModule()

    cObj = BackUpFile()
    
    if(len(sys.argv) == 3):
        cObj.Accept(sys.argv)   

        Ret = cObj.CheckFileAndDirectoryPath()
    
        if(Ret == True):
            cObj.ScheduleToBackupFile() 

    else:
        print("Invalid number of arguments")
    

if __name__ == "__main__":
    main()

    