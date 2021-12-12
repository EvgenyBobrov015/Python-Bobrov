n = input("Введите число от 1 до 12: ")
seasons_dict = {"Зима": (1, 2, 12),
                "Весна": (3, 4, 5),
                "Лето": (6, 7, 8),
                "Осень": (9, 10, 11)}
month_list = ["Январь",
              "Февраль",
              "Март",
              "Апрель",
              "Май",
              "Июнь",
              "Июль",
              "Август",
              "Сентябрь",
              "Октябрь",
              "Ноябрь",
              "Декабрь"]

if n.isdigit() and 0 < int(n) <= 12:
    n = int(n)
    for k in seasons_dict.keys():
        if n in seasons_dict[k]:
            print(f"Время года: {k}")

    for i, v in enumerate(month_list):
        if n == i + 1:
            print(f"Месяц: {month_list[i]}")
else:
    print("Вы ввели некорректные данные!!")
