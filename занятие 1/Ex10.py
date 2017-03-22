ch=(str(input("Введите символ")))
s=['0','1','2','3','4','5','6','7','8','9']
sum=0
for i in range (0,len(s)):
    if (ch==s[i]):
        sum=sum+1
if (sum==1):
    print("yes")
else:
    print("no")