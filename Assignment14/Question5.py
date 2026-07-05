# Write a lambda function which accept one numbers and return True if number is even otherwise False

from Assignment14_Module import DisplayModule,lambdaEvenNumber

EvenNumber = lambda Num : Num % 2 == 0

def main():

    DisplayModule()

    Number = int(input("Enter the number : "))
    
    Ret = EvenNumber(Number)

    if Ret == True:
        print(f"Number {Number} is Even")


    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Number = int(input("Enter the number : "))
    
    Ret = lambdaEvenNumber(Number)

    if Ret == True:
        print(f"Number {Number} is Even")

if __name__ == "__main__":
    main()