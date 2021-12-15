n, v = 0, 0
while v != "q":
    j = n
    my_list = input("Введите числа через пробел(завершить-'q'): ").split()
    for i, v in enumerate(my_list):
        try:
            v = int(v)
            n = n + v
        except ValueError:
            if v == "q":
                print("Программа завершена!")
                break
            else:
                print("Err")
    j = n - j
    if v == "q":
        print(f"Результат: {n}")
    else:
        print(f"Результат: {n}({j})")
