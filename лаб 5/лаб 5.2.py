arr=[]
brr=[]
a1=0
b1=0
for i in range(0,8):
    arr.append(int(input("Введите элемент массива")))
    if (arr[i]>=10)and(arr[i]<100):
        a1=arr[i]%10
        b1=arr[i]//10
        brr.append(a1+b1)
print(brr)
