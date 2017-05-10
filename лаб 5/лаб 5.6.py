arr=[]
brr=[]
min=0
jmax=0
imax=0
max=0
n=int(input("Введите количество строк"))
m=int(input("Введите количество столбцов"))
for i in range (0,n):
    arr.append([])
    for j in range (0,m):
        arr[i].append(int(input("Введите элемент матрицы")))
for i in range (0,n):
    min = arr[i][0]
    jmax=0
    for j in range (1,m):
        if arr[i][j]<min:
            min=arr[i][j]
            jmax=j
    brr.append(min)
    brr.append(jmax)
print(brr)
max=brr[0]
for k in range (1,len(brr)):
    if k%2==0:
       if brr[k]>max:
           max=brr[k]
           jmax=brr[k+1]
           imax=k//2
print(max)
print(imax,jmax)







