summ=1
n=(int(input("Введите количество слагаемых")))
x=(float(input("Введите число")))
i=1
fact=1
while i!=n:
    fact=fact*i
    summ=summ+((i*2+1)*x**(i*2))/fact
    i+=1
print(summ)