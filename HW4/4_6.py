from itertools import count, cycle

my_el = int(input("Введите число с которого сгенерировать числа: "))
my_list = []
try:
    my_el = int(my_el)
except ValueError:
    print("Данные некорректны!")
else:
    for i in count(my_el):
        if i > my_el + 8:
            break
        else:
            my_list.append(i)
    print("Полученые числа: ", str(my_list).replace('[', '').replace(']', ''))

    print("Повторение элементов списка:")
    h = 0
    for k in cycle(my_list):
        if h > 20:
            break
        print(k)
        h += 1
