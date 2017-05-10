arr=[]
countch=0
countnch=0
n=int(input("Введите количество строк"))
m=int(input("Введите количество столбцов"))
for i in range (0,n):
    arr.append([])
    for j in range (0,m):
        arr[i].append(int(input("Введите элемент матрицы")))
        if arr[i][j]%2==0:
            countch=countch+1
        else:
            countnch=countnch+1
print(arr)
print("chetnie",countch)
print("nechetnie",countnch)
