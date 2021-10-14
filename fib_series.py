def fibonacci(n):
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


print("fibonacci series")
print("----------")
n = int(input("enter n value: "))
for i in range(n+1):
    print(fibonacci(i))