mouth=int(input("Введите месяц"))
if (mouth >= 3) and (mouth < 6):
    print("Время года- Весна")
else:
    if (mouth>=6)and(mouth<9):
        print("Время года-Лето")
    else:
        if (mouth>=9)and(mouth<12):
            print("Время года-Осень")
        else:
            if ((mouth>0)and(mouth<=2))or(mouth==12):
                print("Время года-Зима")
            else:
                print("Error")


