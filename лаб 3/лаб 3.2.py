x=float(input("Введите число"))
n=float(input("Введите n"))
proiz=1
i=1
k=1
s=0
p=1
while i<=n:
    if ((i-5)*x**i)==0:
        print("error")
    else:
        s=s+((-1)**(3*i+1))/((i-5)*(x**i))
    while k<=(i+7):
        if (k - 2) == 0:
           print(k," ","Delenie na 0")
        else:
            p=p*(((k**2)-9)/(k-2))
            proiz = proiz * s * p
        k+=1
    i+=1
print(proiz)

