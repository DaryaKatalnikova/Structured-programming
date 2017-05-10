arr=[]
count=0
k=(int(input("Введите число")))
n=(int(input("Введите число строк")))
m=(int(input("Введите число столбцов")))
for i in range (0,n):
    arr.append([])
    for j in range (0,m):
        arr[i].append(int(input("Введите элемент матрицы")))
        if k==arr[i][j]:
            count=count+1
print("kolvo=",count)