n = 0
total = 0
def printing_average():
    global n, total
    if n == 5:
        print("The average is =", total / n)
        print("Total =", total)
        print("n =", n)
    else :
         num = int(input("Enter a number\n"))
         total = total + num
         n += 1
         printing_average()
printing_average() 