# Write a program which contains one lambda function which accepts one parameter and return power of two.
# Input : 4   Output : 16
# Input : 6   Output : 64

from Assignment19_Module import DisplayModule

PowerOfTwo = lambda No : No ** 2

def main():
    DisplayModule()

    print("\n")
    
    Number = int(input("Enter the number : "))
    
    Ret =  PowerOfTwo(Number)

    print(f"Power of two for {Number} is : {Ret}")

if __name__ == "__main__":
    main()