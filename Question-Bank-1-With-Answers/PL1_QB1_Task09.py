def printing_num(n = 0):
    if n == 10:
         print()
    else :
         print(n)
         printing_num(n+1)
printing_num()    