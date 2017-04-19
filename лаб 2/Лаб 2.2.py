price=float(input("Введите стоимость "))
sale=0
if ((price>400)and(price<600)):
    print("Скидка 5%")
    print("Стоимость= ",price-(price*0.05))
else:
    if ((price>600)and(price<1000)):
        print("Скидка 10%")
        print("Стоимость= ", price-(price*0.1))