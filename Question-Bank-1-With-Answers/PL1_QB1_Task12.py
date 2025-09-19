total = 0 
#c = 0
def printing_sum(n = 1):
    global total, c
    if n > 100:
        print("Sum of the numbers =", total)
        #print(c)
    else :
        total = total + n
        #c += 1
        printing_sum(n+1)
printing_sum()    