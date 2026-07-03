lambdaDisplaySquareModule = lambda value:value * value
lambdaDisplayCubeModule = lambda value:value * value * value
lambdaDivisibleByModule = lambda value:value % 3 == 0 and value % 5 == 0

def DisplayAcceptedInputModule(value):
    print(value)

def DisplayModule():
    print("Jay Ganesh")

def listInputChkGreaterModule(Data):
    GreateNumber = 0
    for no in Data:
        if(no > GreateNumber):
            GreateNumber = no
        
    print(GreateNumber, "is greater")

def ChkGreaterModule(No1,No2):
    if (No1 > No2):
        print(No1, "is greater")
    else:
        print(No2, "is greater")

def DisplaySquareModule(value):
    Square = value * value
    print("Square of ",value," is : ",Square)
    
def DisplayCubeModule(value):
    Cube = value * value * value
    print("Cube of ",value," is : ",Cube)
    
def DivisibleByModule(value):
    if value % 3 == 0 and value % 5 == 0:
        print(value, " is divisible by 3 and 5")
    else:
        print(value, " is not divisible only by 3 and 5")