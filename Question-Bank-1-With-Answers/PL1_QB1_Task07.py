f_number = int(input("Enter your first number\n"))
s_number = int(input("Enter your second number\n"))

if f_number > s_number:
    result = f_number - s_number
    print("Result = ", result)
else:
    result = s_number - f_number
    print("Result = ", result)