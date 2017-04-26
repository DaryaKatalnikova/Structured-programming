m=int(input("Введите левую границу"))
n=int(input("Введите правую границу"))
summa=0
while m<=n:
    if (m%2==1):
        summa=summa+m**2
    m+=1
print(summa)