def IsVowelModule(Char):
    Vowels = ['a','e','i','o','u']

    for Ch in Vowels:
        if Ch == Char.lower():
            return True
        
    return False

def FactorModule(No):
    Factor = ""
    for i in range(1,No+1):
        if No % i == 0:
            Factor += str(i) + " "

    return Factor

def CalculationsModule(No1, No2):
    Addition = No1 + No2
    Substraction = No1 - No2
    Multiplication = No1 * No2
    Division = No1 / No2

    return Addition,Substraction,Multiplication,Division

def PrintNumbersModule(Number):
    StrNumbers = ""
    for i in range(1, Number+1):
        StrNumbers += str(i) + " "

    return StrNumbers

def PrintReverseNumbersModule(Number):
    StrNumbers = ""
    for i in range(Number,0,-1):
        StrNumbers += str(i) + " "

    return StrNumbers