import os
import sys
import datetime
import hashlib
import time
import re
import smtplib
import schedule
from email.message import EmailMessage


class DuplicateFileRemoval:

    def __init__(self):
        self.DirectoryPath = ""
        self.TimeInterval = ""
        self.Email = ""
        self.Timestamp = ""
        self.CheckSumList = list()
        self.LogDetails = {}

    def SendNotification(self, message,LogFileName):
        sender_email = "omkarpataskarpython@gmail.com"
        app_password = "your_app_password"
        self.LogDetails["EmailStatus"] = []
        email = EmailMessage()
        email["From"] = sender_email
        email["To"] = self.Email
        email["Subject"] = "Duplicate File Removal Automation"

        email.set_content(message)

        # Attach file
        if LogFileName and os.path.exists(LogFileName):
            with open(LogFileName, "rb") as file:
                file_data = file.read()
                file_name = os.path.basename(LogFileName)

            email.add_attachment(
                file_data,
                maintype="application",
                subtype="octet-stream",
                filename=file_name
            )

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()

            server.login(sender_email, app_password)

            server.send_message(email)

            server.quit()
            # Email success status
            self.LogDetails['EmailStatus'].append({
                "Status": "Sent",
                "Time": datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                "Receiver": self.Email
            })
            self.WriteLogFile(2)

        except Exception as e:
             # Email failure status
            self.LogDetails['EmailStatus'].append({
                "Status": "Failed",
                "Time": datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S"),
                "Receiver": self.Email,
                "Error": str(e)
            })
            self.WriteLogFile(2)

    def GetTimestamp(self):
        self.Timestamp = datetime.datetime.now()
        return self.Timestamp

    def WriteLogFile(self,OperationLogs=1):
        log_folder = "Logs"
        LogFileName = "DuplicateRemovalLog_%s.log"%str(self.Timestamp.strftime("%d_%m_%Y_%H_%M_%S"))
        os.makedirs(log_folder, exist_ok=True)

        Border="-"*65

        self.Timestamp = self.GetTimestamp()
        LogFileName = os.path.join(log_folder, LogFileName)
        
        fObj = open(LogFileName,"a")
        if(OperationLogs == 1):
            fObj.write(Border+"\n")
            fObj.write("Marvellous Automation Script\n")
            fObj.write(Border+"\n")
            fObj.write(f"\nStarting time of directory scanning  : {self.LogDetails['StartScanTime'][0]} \n")
            fObj.write(f"\nCompletion time of directory scanning  : {self.LogDetails['ScanComplitionTime'][0]}\n")
            fObj.write("\nName of the directory scanned : \n")
            for value in self.LogDetails['ScannedDirectoryName']:
                fObj.write(value+"\n")

            fObj.write(f"\nTotal number of files scanned : {self.LogDetails['TotalNumberOfFilesScanned'][0]} \n")
            fObj.write(f"\nTotal number of duplicate files found  : {self.LogDetails['TotalDuplicateFilesFound'][0]} \n")
            fObj.write(f"\nTotal number of duplicate files deleted   : {self.LogDetails['TotalDeletedFiles'][0]} \n")

            fObj.write("\nComplete paths of all deleted duplicate files  : \n")
            for value in self.LogDetails['DeletedFilesPath']:
                fObj.write(value+"\n")

            fObj.write("\nChecksum values of duplicate files  : \n")
            for value in self.LogDetails['DuplicateFilesChecksum']:
                fObj.write(value+"\n")
            fObj.write(Border+"\n")

            fObj.close()

            fReadObj = open(LogFileName,"r")
            content = fReadObj.read()
            headerMessage = '''
Jay Ganesh,

The duplicate-file removal operation has been completed successfully.

Operation Statistics: \n'''

            footerMessage = '''
\nPlease find the detailed log file attached to this email.

Regards,
Marvellous Automation System
    '''
            message = headerMessage + content + footerMessage

            self.SendNotification(message,LogFileName) 

        else:
            fObj.write(f"\n{Border}\n")
            fObj.write("\nEmail Status  : \n")

            for email_status in self.LogDetails['EmailStatus']:
                fObj.write(f"Status   : {email_status['Status']}\n")
                fObj.write(f"Time     : {email_status['Time']}\n")
                fObj.write(f"Receiver : {email_status['Receiver']}\n")

                if "Error" in email_status:
                    fObj.write(f"Error    : {email_status['Error']}\n")

                fObj.write("\n")

            fObj.write(f"\n{Border}\n")
        


    def CalculateCheckSum(self,FileName):
        fObj = open(FileName,"rb")

        hObj = hashlib.md5()

        buffer = fObj.read(1000)

        while(len(buffer) > 0):
            hObj.update(buffer)
            buffer = fObj.read(1000)

        fObj.close()

        return hObj.hexdigest()
    
    def FindDuplicate(self):
        Duplicates = {}
        self.LogDetails['ScannedDirectoryName'] = []
        self.LogDetails['DuplicateFilesChecksum'] = []
        self.LogDetails['TotalNumberOfFilesScanned'] = []
        TotalNumberOfFilesScanned = 0
        for FolderName,SubFolder,FileName in os.walk(self.DirectoryPath):
            self.LogDetails['ScannedDirectoryName'].append(FolderName)
            for fName in FileName:
                TotalNumberOfFilesScanned += 1
                fName = os.path.join(FolderName,fName)
                CheckSum = self.CalculateCheckSum(fName)

                if CheckSum in Duplicates:
                    Duplicates[CheckSum].append(fName)
                    self.LogDetails['DuplicateFilesChecksum'].append(CheckSum)
                else:
                    Duplicates[CheckSum] = [fName]
        self.LogDetails['TotalNumberOfFilesScanned'].append(TotalNumberOfFilesScanned)
        return Duplicates
        
    def DeleteDuplicate(self):
        
        self.LogDetails['DeletedFilesPath'] = []
        self.LogDetails['TotalDuplicateFilesFound'] = []
        self.LogDetails['TotalDeletedFiles'] = []
        self.LogDetails['StartScanTime'] = []
        self.LogDetails['ScanComplitionTime'] = []
        self.LogDetails['StartScanTime'].append(self.GetTimestamp())
        start_time = time.perf_counter()
        
        MyDict = self.FindDuplicate()
        Result = list(filter(lambda x: len(x) > 1,MyDict.values()))
        Count = 0
        TotalDeleted = 0
        TotalDuplicateFilesFound = 0
        for value in Result:
            for SubValue in value:        
                TotalDuplicateFilesFound += 1
                Count += 1
                if(Count>1):
                    self.LogDetails['DeletedFilesPath'].append(SubValue)
                    os.remove(SubValue)
                    TotalDeleted += 1
            Count = 0
        end_time =time.perf_counter()

        TimeRequired = end_time - start_time
        self.LogDetails['ScanComplitionTime'].append(f"{TimeRequired:.5f}")
        self.LogDetails['TotalDuplicateFilesFound'].append(TotalDuplicateFilesFound)
        self.LogDetails['TotalDeletedFiles'].append(TotalDeleted)

        self.WriteLogFile(1)
        
    def Accept(self):
        self.DirectoryPath = sys.argv[1]
        self.TimeInterval = int(sys.argv[2])
        self.Email = sys.argv[3]

    def Validation(self):

        if(len(sys.argv) == 2):
            if(sys.argv[1].lower() == "--h" or sys.argv[1].lower == "--help"):
                HelpInformation = '''
                Help information:
*************************************************************************************

Purpose : Duplicate File Removal Automation

*************************************************************************************

This script 
scans a directory, 
identifies duplicate files using checksums,
deletes duplicate files, 
creates a log file, 
and sends the log file through email.

*************************************************************************************

Usage:
******

- python DuplicateFileRemoval.py <DirectoryPath> <IntervalInMinutes> <ReceiverEmail>

Example:
********

- python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

*************************************************************************************

Marvellous Infosystems : Python- Automation & Machine Learning

*************************************************************************************

    '''
                print(HelpInformation)

            elif(sys.argv[1].lower() == "--u"  or sys.argv[1].lower() == "--usage"):
                UsageInformation = '''
                        Usage information
*************************************************************************************

Purpose : Duplicate File Removal Automation

*************************************************************************************

Usage:
******

python DuplicateFileRemoval.py <AbsoluteDirectoryPath> <TimeIntervalInMinutes> <ReceiverEmailAddress>

Example:
********

- python DuplicateFileRemoval.py E:/Data/Demo 50 marvellousinfosystem@gmail.com

*************************************************************************************

Marvellous Infosystems : Python- Automation & Machine Learning

*************************************************************************************
'''
                print(UsageInformation)
            return -7

        if(len(sys.argv) == 4):
            
            if(not os.path.isabs(sys.argv[1])):
                return -2

            if(not os.path.exists(sys.argv[1])):
                return -3
            
            if(not os.path.isdir(sys.argv[1])):
                return -4

            if(not os.access(sys.argv[1], os.R_OK)):
                return -5

            if(not sys.argv[2].isnumeric()):
                return -6

            if(int(sys.argv[2]) <= 0):
                return -7

            pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

            if(not re.match(pattern, sys.argv[3])):
                return -8
            
            
        else:
            return -1

        return 1
    


def main():

    cObj = DuplicateFileRemoval()

    Ret = cObj.Validation()
    if(Ret == 1):
        cObj.Accept()
        # cObj.DeleteDuplicate()
        schedule.every(cObj.TimeInterval).seconds.do(cObj.DeleteDuplicate)

        while True:
            schedule.run_pending()
            time.sleep(1)
    elif(Ret == -1):
        print("Invalid number of Arguments")
    elif(Ret == -2):
        print("Please enter absolute path of directory")
    elif(Ret == -3):
        print("Directory does not exists")
    elif(Ret == -4):
        print("Not a directory")
    elif(Ret == -5):
        print("No read permission")
    elif(Ret == -6):
        print("Not a number")
    elif(Ret == -7):
        print("Interval should be greater than zero")
    elif(Ret == -8):
        print("Invalid email format")


if __name__ == "__main__":
    main()