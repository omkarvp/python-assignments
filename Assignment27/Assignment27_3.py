# 3: Write a Python program to implement a class named Numbers with the following specifications:
# •	The class should contain one instance variable: 
# o	Value 
# •	Define a constructor (__init__) that accepts a number from the user and initializes Value. 
# •	Implement the following instance methods: 
# o	ChkPrime() – returns True if the number is prime, otherwise returns False. 
# o	ChkPerfect() – returns True if the number is perfect, otherwise returns False. 
# o	Factors() – displays all factors of the number. 
# o	SumFactors() – returns the sum of all factors. 
# •	Create multiple objects and call all methods.

from Assignment27_Module import DisplayModule

class Numbers:

    def __init__(self,Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        
        if self.Value == 2:
            return True
        
        if self.Value % 2 == 0:
            return False
        
        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False
        
        return True

    def ChkPerfect(self):
        if self.Value <= 1:
            return False
        
        Sum = 1
        SquareRoot = int(pow(self.Value, 0.5))
        for i in range(2,SquareRoot+1):
            if self.Value % i == 0:
                Sum += i
                if i != self.Value // i:
                    Sum += self.Value // i
                    
        return Sum == self.Value

    def Factors(self):
        Factorstr = ""
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                Factorstr += str(i) + " "

        print(f"Factors of {self.Value} are : {Factorstr}")
    
    def SumFactors(self):
        SumOfFactors = 0
        for i in range(1,self.Value+1):
            if self.Value % i == 0:
                SumOfFactors += i 

        print(f"Sum of factors for {self.Value} is : {SumOfFactors}")

DisplayModule()

Obj = Numbers(25)

IsPrime = Obj.ChkPrime()
if IsPrime == True:
    print(f"{Obj.Value} is Prime Number")
else:
    print(f"{Obj.Value} is not Prime Number")

IsPerfect = Obj.ChkPerfect()
if IsPerfect == True:
    print(f"{Obj.Value} is Perfect Number")
else:
    print(f"{Obj.Value} is not Perfect Number")

Obj.Factors()

Obj.SumFactors()