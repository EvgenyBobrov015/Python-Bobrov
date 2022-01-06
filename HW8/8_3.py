class OnlyNum(Exception):
    def __init__(self, n):
        self.n = n

    def __str__(self):
        return "Ввдодите только числа!!"


class InList:
    my_list = []

    def __init__(self, var):
        self.var = var

    def nums(self):
        if self.var.isdigit():
            InList.my_list.append(self.var)
        elif self.var == "stop":
            return
        else:
            raise OnlyNum(self.var)


in_def = 0
while in_def != "stop":
    in_def = input("Введите данные: ")
    var1 = InList(in_def)
    try:
        var1.nums()
    except OnlyNum:
        print("Ввдодите только числа!!")
print(f"Получившийся список: {InList.my_list}")
