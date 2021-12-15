def my_func(s_1, s_2):
    try:
        s_1 = float(s_1)
        s_2 = float(s_2)
        num = s_1 / s_2
    except (ValueError, ZeroDivisionError):
        print("Данные некорректны!")
    else:
        print(f"Результат деления: {num}")


my_func(input("Введите первое число: "), input("Введите второе число: "))
