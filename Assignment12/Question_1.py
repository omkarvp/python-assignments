# Write a program which accepts one character and checks whether it is vowel or not
# Input: a
# Output: Vowel
from Assignment12_Module import IsVowelModule

def IsVowel(Char):
    Vowels = ['a','e','i','o','u']

    for Ch in Vowels:
        if Ch == Char.lower():
            return True
        
    return False


def Display():
    print("="*5,"Jay Ganesh","="*4)

def main():
    print("*"*21)
    Display()
    print("*"*21)

    print("*"*21)
    print("=====Vowels====")
    print("*"*21)

    Character = input("Enter one character : ")
    Ret = IsVowel(Character)

    if Ret:
        print(Character,"is Vowel")
    else:
        print(Character,"is not Vowel")

    print("*"*21)
    print("*"*5,"Using Module Function","*"*6)
    print("*"*21)

    Character1 = input("Enter one character : ")
    Ret1 = IsVowelModule(Character1)

    if Ret1:
        print(Character1,"is Vowel")
    else:
        print(Character1,"is not Vowel")


if __name__ == "__main__":
    main()