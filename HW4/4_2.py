from random import randint

my_list = [randint(1, 150) for k in range(12)]
new_list = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print("Заданый список: ", my_list)
print("Полученый список: ", new_list)
