def fact(n):
    try:
        n = int(n)
    except ValueError:
        print("Некорректные данные!")
    else:
        k = 1
        for i in range(1, n + 1):
            k = i * k
            yield i, k


for c, el in fact(input("Введите число: ")):
    print(f"{c}! = {el}")
