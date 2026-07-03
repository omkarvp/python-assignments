# Write a program which accepts one number and check whether number is palindrome or not
# Input: 121
# Output: Palindrome
from Assignment11_Module import isPalindromeUsingIntModule,isPalindromeUsingStrModule
def isPalindromeUsingInt(Number):
    ReverseString = ""
    strNumber = str(Number)
    for i in range(len(strNumber)-1, -1,-1):
        ReverseString += strNumber[i]

    if int(ReverseString) == int(Number):
        return True
    
    return False

def isPalindromeUsingStr(Number):
    ReverseString = ""
    for i in range(len(Number)-1, -1,-1):
        ReverseString += Number[i]

    if ReverseString == Number:
        return True
    
    return False
    
def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)
    print("*"*21)
    print("=====Palindrome Number====")
    print("*"*21)

    Number = input("Enter the number : ")

    Ret = isPalindromeUsingStr(Number)
    if Ret:
        print("Using str Data type",Number,"is Palindrome")
    else:
        print("Using str Data type",Number,"is Not Palindrome")
    
    print("*"*21)
    print("=====Palindrome Number====")
    print("*"*21)

    Number1 = input("Enter the number : ")

    Ret1 = isPalindromeUsingInt(Number1)

    if Ret1:
        print("Using int Data type",Number1,"is Palindrome")
    else:
        print("Using int Data type",Number1,"is Not Palindrome")
    

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)


    Number2 = input("Enter the number : ")

    Ret2 = isPalindromeUsingStrModule(Number2)
    if Ret2:
        print("Using str Data type",Number2,"is Palindrome")
    else:
        print("Using str Data type",Number2,"is Not Palindrome")
    
    print("*"*21)
    print("=====Palindrome Number====")
    print("*"*21)

    Number3 = input("Enter the number : ")

    Ret3 = isPalindromeUsingIntModule(Number3)

    if Ret3:
        print("Using int Data type",Number3,"is Palindrome")
    else:
        print("Using int Data type",Number3,"is Not Palindrome")

if __name__ == "__main__":
    main()