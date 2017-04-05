a=int(input("Введите первое число"))
b=int(input("Введите второе число"))
f=int(input("Введите третье число"))
if ((a+b>f)and(a+f>b)and(b+f>a)):
    print("Да")
else:
    print("Нет")