def power(b,e):
    if(e==0):
        return 1
    else:
        return b*power(b,e-1)

b = int(input("enter the base integer: "))
e = int(input("enter the exponent integer: "))
print(power(b,e))