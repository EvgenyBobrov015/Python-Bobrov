income = float(input("Введите ваш доход: "))
expenses = float(input("Введите ваши расходы: "))
profit = income - expenses
if income > expenses:
    print(f"Ваша фирма получла прибыль в размере: {profit} руб.")
    print(f"Рентабельность вашей фирмы составила: {profit / income:.2f} ")
    staff = int(input("Введите количество сотрудников в вашей фирме: "))
    print(f"Прибыль фирмы в расчете на одного сотрудника составила: {profit / staff} руб.")
elif income < expenses:
    print(f"К сожалению, ваша фирма сработала в убыток. Вы потеряли: {profit * -1} руб. :(")
else:
    print("Ваша фирма сработала в ноль!")
