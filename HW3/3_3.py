def my_func(var1, var2, var3):
    try:
        var1, var2, var3 = int(var1), int(var2), int(var3)
    except ValueError:
        print("Err")
    else:
        my_list = [var1, var2, var3]
        my_list.remove(min(var1, var2, var3))
        summa = sum(my_list)
        print(f"Result: {summa}")


my_func(input("Var1: "), input("Var2: "), input("Var3: "))
