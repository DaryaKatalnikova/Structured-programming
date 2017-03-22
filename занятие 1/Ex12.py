s=(str(input("Введите строку")))
sum=0
for i in range (0,len(s)//2):
    if (s[i]==s[-i-1]):
        sum=sum+1
if (sum==len(s)//2):
    print("Палиндром")
else:
    print("Не палиндром")
