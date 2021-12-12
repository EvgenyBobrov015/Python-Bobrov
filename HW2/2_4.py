my_list = input("Введите строку: ").split()

for i, v in enumerate(my_list, 1):
    v = v[:10]
    print(f"{i}) {v}")
