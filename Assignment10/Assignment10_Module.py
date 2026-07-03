def MultiplicationTableModule(value):
    table = ""
    mult = 0
    for i in range(1,11):
        mult = i * value
        table = table + str(mult) + " "

    print(table)

def SumOfNaturalNumberModule(value):
    SumOfNaturalNumbers = 0
    
    for i in range(1,value+1):
        if type(i) == int and i > 0:
            SumOfNaturalNumbers += i    

    print(SumOfNaturalNumbers)

def DisplayFactorialNumberModule(value):
    FactorialNumbers = 1
    for i in range(1,value+1):
        FactorialNumbers = FactorialNumbers*i
    
    if value > 0:
        print("Factorial is :",FactorialNumbers)
    else:
        print("Number should be greater than 0")

def DisplayAllEvenNumberModule(value):
    AllEvenNumbers = ""
    for i in range(1,value+1):
        if i % 2 == 0:
            AllEvenNumbers += str(i) + " "
    if value > 1:
        print("All Even numbers till the",value,"are :",AllEvenNumbers)
    else:
        print("Number should be greater than 1")

def DisplayAllOddNumberModule(value):
    AllOddNumbers = ""
    for i in range(1,value+1):
        if i % 2 != 0:
            AllOddNumbers += str(i) + " "
    if value > 1:
        print("All Odd numbers till the",value,"are :",AllOddNumbers)
    else:
        print("Number should be greater than 1")