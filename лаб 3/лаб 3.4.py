m=1
n=1000
delenie=0
k=int(input("Введите число"))
while m<=n:
    if (m<100):
        pass
    else:
        if (m==1000):
            if ((((m//100)%10)**2)%5==0):
                print(m, ((m // 100)%10) ** 2 / k)
        else:
            if (((m//100)**2)%5==0):
                print(m,(m//100)**2/k)
    m+=1

