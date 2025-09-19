def evenOrOdd(c = 1):
    if c > 5:
        print("Program has ended")
    else:    
        num = int(input("Enter a number\n"))
        if num % 2 == 0:
            print("Number is even")
        else:
            print("Number is odd")    
        evenOrOdd(c+1)
evenOrOdd()