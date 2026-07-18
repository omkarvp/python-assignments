# 2: Write a Python program to implement a class named BankAccount with the following requirements:
# •	The class should contain two instance variables: 
# o	Name (Account holder name) 
# o	Amount (Account balance) 
# •	The class should contain one class variable: 
# o	ROI (Rate of Interest), initialized to 10.5 
# •	Define a constructor (__init__) that accepts Name and initial Amount. 
# •	Implement the following instance methods: 
# o	Display() – displays account holder name and current balance. 
# o	Deposit() – accepts an amount from the user and adds it to the balance. 
# o	Withdraw() – accepts an amount from the user and subtracts it from the balance.
# (Ensure withdrawal is allowed only if sufficient balance exists.) 
# o	CalculateInterest() – calculates and returns interest using the formula: 
# Interest = (Amount * ROI) / 100
# •	Create multiple objects and demonstrate all methods. 

from Assignment27_Module import DisplayModule

class BankAccount:
    ROI = 10.5

    def __init__(self, Name,InitialAmount):
        self.Name = Name
        self.Amount = InitialAmount
        
    def Display(self):
        print(f"Account holder name is : {self.Name} and current balance is : {self.Amount}") 

    def Deposit(self):
        DepositAmount = float(input("Enter the deposit amount : "))
        self.Amount += DepositAmount
        print(f"Account holder name is : {self.Name} and current balance is : {self.Amount:.2f}")

    def Withdraw(self):
        WithdrawAmount = float(input("Enter the withdraw amount : "))
        if self.Amount > WithdrawAmount:
            self.Amount -= WithdrawAmount
            print(f"Account holder name is : {self.Name} and current balance is : {self.Amount:.2f}")
        else:
            print(f"Sorry Insufficient balance. Current balance is : {self.Amount:.2f} and tried to withdraw is : {WithdrawAmount}")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Account holder name is : {self.Name} and current balance is : {self.Amount:.2f} and interest is : {Interest}")

Obj = BankAccount("Omkar Pataskar", 4000)
Obj.Display()
Obj.Deposit()
Obj.Withdraw()
Obj.CalculateInterest()