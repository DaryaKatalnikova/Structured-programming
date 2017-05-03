s1=input("Введите первое слово")
s2=input("Введите второе слово")
s3=input("Введите третье слово")
ss=' '
i=0
j=0
k=0
for i in range(len(s1)):
    for j in range(len(s2)):
        for k in range(len(s3)):
            if s1[i]==s2[j]==s3[k]:
                ss=ss+s1[i]
print(ss)
