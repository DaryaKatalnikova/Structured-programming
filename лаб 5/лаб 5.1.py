arr=[]
sum=0
count=0
for i in range(0,13):
    arr.append(int(input("Введите элемент массива")))
    if (arr[i]%2==0)and(arr[i]>=0):
        sum=sum+arr[i]
        count=count+1
print("sum=",sum)
print("count=",count)