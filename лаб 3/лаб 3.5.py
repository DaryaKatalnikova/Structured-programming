n = (int(input("Введите количество значении ")))
a = [int(input("Значение массива ")) for x in range(n)]
i=0
proizv=1
while a[i] != 0:
    if a[i]<0:
        proizv=proizv*a[i]
    i+=1
print(proizv)
