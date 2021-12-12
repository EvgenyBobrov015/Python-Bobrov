my_list = [10, 8, 7, 7, 4, 2, 2]
n = input("Введите оценку от 1 до 10: ")

if n.isdigit() and 0 < int(n) <= 10:
    n = int(n)
    for i in range(0, len(my_list)):
        if my_list[i] < n:
            my_list.insert(i, n)
            print(my_list)
            break
        elif my_list[-1] >= n:
            my_list.append(n)
            print(my_list)
            break
else:
    print("Вы ввели некорректные данные!!")
