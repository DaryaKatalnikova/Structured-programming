x=float(input("Введите координату х"))
y=float(input("Введите координату y"))
if (y>=-1)and(y<=1)and(((x<=y)and(x>=-y))or((x>=y)and(x<=-y))):
    print("yes")
else:
    print("no")

