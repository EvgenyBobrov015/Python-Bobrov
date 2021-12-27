my_file = open("my_file1.txt", "a", encoding="utf-8")
string = 1
while True:
    string = input("Введите строку (для завершения нажмите Enter):\n")
    if string != "":
        my_file.write(f"{string}\n")
    else:
        break
print("Запись завершена!")
my_file.close()
