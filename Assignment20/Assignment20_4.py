# Design a Python application that creates three threads named Small, Capital, and Digits.
# All threads should accept a string as input. 
# The Small thread should count and display the number of lowercase characters. 
# The Capital thread should count and display the number of uppercase characters. 
# The Digits thread should count and display the number of numeric digits. 
# Each thread must also display: 
#   Thread ID 
#   Thread Name




import threading
from Assignment20_Module import DisplayModule

def Small(InputString):
    LengthOfStr = len(InputString)
    SmallCounter = 0
    LowerCaseCharacters = ""

    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")

    for i in range(LengthOfStr):
        if InputString[i].isalpha() and InputString[i].islower():
            SmallCounter += 1
            LowerCaseCharacters += InputString[i]
    print(f"The count of lowercase characters is : {SmallCounter} and lowercase characters are : {LowerCaseCharacters}")
    print("")

def Capital(InputString):
    LengthOfStr = len(InputString)
    CapitalCounter = 0
    CapitalCaseCharacters = ""

    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")
    
    for i in range(LengthOfStr):
        if InputString[i].isalpha() and InputString[i].isupper():
            CapitalCounter += 1
            CapitalCaseCharacters += InputString[i]
    print(f"The count of uppercase characters is : {CapitalCounter} and lowercase characters are : {CapitalCaseCharacters}")
    print("")

def Digits(InputString):
    LengthOfStr = len(InputString)
    DigitsCounter = 0
    DigitsCharacters = ""

    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")

    for i in range(LengthOfStr):
        if InputString[i].isnumeric():
            DigitsCounter += 1
            DigitsCharacters += InputString[i]
    print(f"The count of digit characters is : {DigitsCounter} and lowercase characters are : {DigitsCharacters}")
    print("")

def main():
    DisplayModule()

    print("")

    StringInput = input("Enter the string : ")
    print("")
    tObjSmall = threading.Thread(target=Small,args=(StringInput,))
    tObjCapital = threading.Thread(target=Capital,args=(StringInput,))
    tObjDigits = threading.Thread(target=Digits,args=(StringInput,))

    tObjSmall.start()
    tObjCapital.start()
    tObjDigits.start()

    tObjSmall.join() # Main should wait until the job of tObjSmall completed 
    tObjCapital.join() # Main should wait until the job of tObjCapital completed
    tObjDigits.join() # Main should wait until the job of tObjDigits completed

if __name__ == "__main__":
    main()