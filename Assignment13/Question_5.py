# Write a program which accepts marks and displays grade
# Conditional Example:
# >= 75 Distinction
# >= 60 First Class
# >= 50 Second Class
# < 50 Fail
from Assignmen_13Module import DisplayGradeModule

def DisplayGrade(Data):
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

def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    Marks = list()
    Marathi = int(input("Enter the martks of Marathi : "))
    Marks.append(Marathi)
    English = int(input("Enter the martks of English : "))
    Marks.append(English)
    Unix = int(input("Enter the martks of Unix : "))
    Marks.append(Unix)
    DataStructure = int(input("Enter the martks of DataStructure : "))
    Marks.append(DataStructure)
    CPPLang = int(input("Enter the martks of CPPLang : "))
    Marks.append(CPPLang)
    Grade = DisplayGrade(Marks)

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Marks1 = list()
    Marathi1 = int(input("Enter the martks of Marathi : "))
    Marks1.append(Marathi1)
    English1 = int(input("Enter the martks of English : "))
    Marks1.append(English1)
    Unix1 = int(input("Enter the martks of Unix : "))
    Marks1.append(Unix1)
    DataStructure1 = int(input("Enter the martks of DataStructure : "))
    Marks1.append(DataStructure1)
    CPPLang1 = int(input("Enter the martks of CPPLang : "))
    Marks1.append(CPPLang1)
    Grade1 = DisplayGradeModule(Marks1)

if __name__ == "__main__":
    main()