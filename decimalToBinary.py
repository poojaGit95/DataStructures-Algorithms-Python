def  deciToBinary(n):
    if(n>=1):
        deciToBinary(n//2)
        print(n%2)

n = int(input("enter decimal integer value: "))
l = deciToBinary(n)