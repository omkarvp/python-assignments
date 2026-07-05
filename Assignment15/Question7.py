# Write a lambda function using filter() which accepts list of strings and returns list of strings having length greater than 5
from Assignment15_Module import DisplayModule,lambdaStringsModule

Strings = lambda String1 : len(String1) > 5

def main():

    DisplayModule()

    Arr = list()

    Element = int(input("Enter the number of strings : "))

    for i in range(Element):
        String = input("Enter string : ")
        Arr.append(String)

    Ret = list(filter(Strings,Arr))

    print(f"Strings having length greater than 5 are : {Ret}")

    print("*"*21)
    print("*"*5,"Using lambda Module","*"*6)
    print("*"*21)

    Arr = list()

    Element = int(input("Enter the number of strings : "))

    for i in range(Element):
        String = input("Enter string : ")
        Arr.append(String)

    Ret = list(filter(lambdaStringsModule,Arr))

    print(f"Strings having length greater than 5 are : {Ret}")

if __name__ == "__main__":
    main()