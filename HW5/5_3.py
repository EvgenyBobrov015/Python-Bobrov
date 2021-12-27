my_list = open("text_3.txt", "r", encoding="utf_8")
content = my_list.read().split("\n")
salary = []
print("Данные сотрудники имеют оклад менее 20000:")
for v in content:
    if float(v.split()[1]) < 20000:
        print(v.split()[0])
    salary.append(float(v.split()[1]))
print(f"Средний оклад сотрудников: {sum(salary) / len(salary)}")
my_list.close()
