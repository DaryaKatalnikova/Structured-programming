x=float(input("Введите количество км в первый день"))
y=float(input("Введите количество км"))
i=1
while x<y:
    x=x+(x*10/100)
    i=i+1
print(i)