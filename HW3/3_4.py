def my_func(x, y):
    try:
        x = float(x)
        y = int(y)
    except ValueError:
        print("Err")
    else:
        if y < 0 < x:
            n = x
            for i in range(1, abs(y)):
                n = n * x
            num = 1 / n
            print(f"Result: {num}")
        else:
            print("Err")


my_func(input("x = "), input("y = "))
