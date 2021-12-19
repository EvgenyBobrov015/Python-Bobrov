from sys import argv

try:
    name, bet, hours, prize = argv
    hours, bet, prize = int(hours), int(bet), int(prize)
except ValueError:
    print("Данные некорректны!!")
else:
    print(f"Ваша часовая ставка: {bet} руб./час")
    print(f"Вы отработали: {hours} час(-а/-ов)")
    print(f"Ваша премия составила: {prize} руб.")
    print(f"Вы заработали: {hours * bet + prize} руб.")
