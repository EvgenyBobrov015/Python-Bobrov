a = float(input("Введите сколько вы пробежали в первый день: "))
b = float(input("Сколько бы вы хотели пробегать: "))
day = 1

while a < b:
    a = a * 1.1
    day += 1

print(day)
