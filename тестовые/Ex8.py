a=[]
sum=0
for i in range (0,6):
   a.append(int(input("Введите число")))
for i in range (1,6):
   if ((a[i]>0) and (a[i-1]>0)) or ((a[i]<0)and(a[i-1]<0)):
      sum=sum+1
if sum>0:
    print("yes")
else:
    print("no")


