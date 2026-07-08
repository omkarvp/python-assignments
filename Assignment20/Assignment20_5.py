# Design a Python application that creates two threads named Thread1 and Thread2.
#   Thread1 should display numbers from 1 to 50. 
#   Thread2 should display numbers from 50 to 1 in reverse order. 
#   Ensure that: 
#       Thread2 starts execution only after Thread1 has completed. 
#   Use appropriate thread synchronization.


import threading
from Assignment20_Module import DisplayModule

def Order():
    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")
    print("")
    
    StringNumber = ""

    for i in range(1,51):
        StringNumber += str(i) + " "

    print(f"Numbers is : {StringNumber}")
    print("")

def ReverseOrder():
    print(f"The Thread name is : {threading.current_thread().name} and the Thread Id is : {threading.get_ident()}")
    print("")
    
    StringNumber = ""

    for i in range(50,-1,-1):
        StringNumber += str(i) + " "

    print(f"Numbers in Reverse order is : {StringNumber}")
    print("")

def main():
    DisplayModule()

    print("")

    tObjSmall = threading.Thread(target=Order)
    tObjSmall.start()
    tObjSmall.join() # Main should wait until the job of tObjSmall completed 

    print("*"*100)

    tObjCapital = threading.Thread(target=ReverseOrder)
    tObjCapital.start()
    tObjCapital.join() # Main should wait until the job of tObjCapital completed


if __name__ == "__main__":
    main()