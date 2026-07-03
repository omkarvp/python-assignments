piValue = 3.14
LambdaAreaModule = lambda Length,Width : Length * Width
LambdaAreaOfCircleModule = lambda radius : piValue * radius * radius

def AreaModule(Length, Width):
    Area = Length * Width
    return Area

def AreaOfCircleModule(radius):
    pi = 3.14 
    Area = pi * radius * radius
    return Area

def isPerfectNumberModule(Num):
    if Num <= 1:
        return False
    
    Sum = 1
    SquareRoot = int(pow(Num, 0.5))
    for i in range(2,SquareRoot+1):
        if Num % i == 0:
            Sum += i
            if i != Num // i:
                Sum += Num // i
                
    return Sum == Num

def DecimalToBinaryModule(num):
    if num == 0:
        return "0"
        
    binary = ""
    while num > 0:
        remainder = num % 2
        binary = str(remainder) + binary
        num = num // 2
    return binary

def DisplayGradeModule(Data):
    TotalMarks = 0
    TotalSubjects = len(Data)

    for marks in Data:
        TotalMarks += marks
    
    TotalMaxMarks = 100 * TotalSubjects
    Percentage = (TotalMarks / TotalMaxMarks) * 100
    print("Percentage : ",Percentage)
    if int(Percentage) >= 75:
        print("Distinction")
    elif int(Percentage) >=60 and int(Percentage) < 75:
        print("First Class")
    elif int(Percentage) >=50 and int(Percentage) < 60:
        print("Second Class")
    else:
        print("Fail")