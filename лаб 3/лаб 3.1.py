x=float(input("Введите число"))
n=int(input("Введите n"))
summa=1
i=1
while i<=n:
    summa=summa+(x*i)/i
    i+=1
print(summa)