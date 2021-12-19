from random import randint

my_list = [randint(1, 20) for k in range(20)]
print("Исходный список: ", my_list)
print("Полученый список: ", list(n for n in my_list if my_list.count(n) == 1))
