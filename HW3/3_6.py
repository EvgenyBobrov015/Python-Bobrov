def int_func(my_str):
    q = 1
    control_list = list("qwertyuiopasdfghjklzxcvbnm ")
    my_str1 = my_str
    my_str1 = list(my_str1)
    for i, v in enumerate(my_str1):
        if v in control_list:
            q = 1
            continue
        else:
            q = 0
            break
    if q == 1:
        print(my_str.title())
    else:
        print("Error")


int_func(input("Enter str: "))
