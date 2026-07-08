lambdaCountDigitModule = lambda Number :len(str(Number))

def isPrimeNumberModule(Number):
    if Number <= 1:
        return False
    
    if Number == 2:
        return True
    
    if Number % 2 == 0:
        return False
    
    # Check divisibility from 2 to n-1
    for i in range(2, Number):
        if Number % i == 0:
            return False
     
    return True

def CountDigitModule(Number):
    Count = len(str(Number))
    return Count

def SumOfDigitUsingIntTypeModule(Number):
    Sum = 0
    Digit = str(Number)
    for i in range(len(Digit)):
        Sum += int(Digit[i])

    return Sum

def SumOfDigitUsingStrTypeModule(Number):
    Sum = 0
    for i in range(len(Number)):
        Sum += int(Number[i])

    return Sum


def ReverseNumberUsingIntTypeModule(Number):
    ReverseString = ""
    Digit = str(Number)
    for i in range(len(Digit)-1, -1,-1):
        ReverseString += Digit[i]

    return ReverseString

def ReverseNumberUsingStrTypeModule(Number):
    ReverseString = ""
    for i in range(len(Number)-1, -1,-1):
        ReverseString += Number[i]

    return ReverseString

def isPalindromeUsingIntModule(Number):
    ReverseString = ""
    strNumber = str(Number)
    for i in range(len(strNumber)-1, -1,-1):
        ReverseString += strNumber[i]

    if int(ReverseString) == int(Number):
        return True
    
    return False

def isPalindromeUsingStrModule(Number):
    ReverseString = ""
    for i in range(len(Number)-1, -1,-1):
        ReverseString += Number[i]

    if ReverseString == Number:
        return True
    
    return False