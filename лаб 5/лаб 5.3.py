arr=[]
brr=[]
count=0
pere=0
for i in range (0,6):
    arr.append(int(input("Введите двоичный элемент массива")))
for i in range (0,6):
    pere=arr[i]
    count=0
    for j in range (0,6):
        if pere==arr[j]:
            count=count+1
    if count<=2:
        brr.append(pere)
print(brr)

        


