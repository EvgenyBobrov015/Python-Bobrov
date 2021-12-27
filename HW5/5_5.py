from random import randint

with open("my_file5", "w+", encoding="utf-8") as my_file:
    my_list = [randint(1, 100) for k in range(10)]
    for i in my_list:
        i = str(i)
        my_file.write(f"{i} ")
    my_file.seek(0)
    new_list = list(map(int, my_file.read().split()))
    print(new_list)
    print(f"Сумма чисел в файле равна: {sum(new_list)}")
