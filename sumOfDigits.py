def sumDigits(n):
    if(n==0):
        return 0
    else:
        x=n%10
        return x+sumDigits(n//10)


n= (int(input("enter your integer: ")))
print(sumDigits(n))