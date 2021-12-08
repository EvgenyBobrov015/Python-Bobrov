print("Давайте узнаем индекс массы вашего тела!")
name = input("Введите ваше имя: ")
weight = float(input("Введите ваш вес в киллограммах: "))
height = float(input("Введите ваш рост в метрах: "))

index = weight / height ** 2

print(f"{name} индекс массы вашего тела: {index:.2f} кг/м2.")
