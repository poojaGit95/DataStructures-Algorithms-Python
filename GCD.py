def gcd(x,y):
    if(x%y==0):
        return y
    else:
        return gcd(y,x%y)


x = int(input("enter 1st integer: "))
y = int(input("enter 2nd integer: "))
print(gcd(x,y))