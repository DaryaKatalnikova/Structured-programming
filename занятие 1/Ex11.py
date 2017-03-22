s=(str(input("Введите строку")))
s=s+" "
sum=0
for i in range (1,len(s)):
    if (s[i]==" "):
        sum=sum+1
print(sum)