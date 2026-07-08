# Write a program which display first 10 even numbers on screen


from Assignment16_Module import DisplayModule 

def firstTenEvenNumbers():
    evenNumberStr = ""

    for i in range(2,21,2):
        evenNumberStr += str( i ) + " "
    
    print(evenNumberStr)

def main():
    DisplayModule()

    firstTenEvenNumbers()

if __name__ == "__main__":
    main()