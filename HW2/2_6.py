n = 0
product_list = []
title_list = []
price_list = []
quantity_list = []
unit_list = []

while True:
    n = n + 1
    print("Введите характеристики товара!")
    title = input("Название: ")
    price = float(input("Цена: "))
    quantity = int(input("Количество: "))
    unit = input("Единицы измерения: ")
    product = (n, {"Название: ": title, "Цена: ": price, "Количество: ": quantity, "ед.: ": unit})
    product_list.append(product)
    title_list.append(title)
    price_list.append(price)
    quantity_list.append(quantity)
    unit_list.append(unit)
    y_n = input("Для добавления товара введите 'Enter', для просмотра аналитики нажмите 'y': ")
    if y_n == "y":
        break
analytics = {"Название: ": title_list, "Цена: ": price_list, "Количество: ": quantity_list, "ед.: ": unit_list}
for i, v in enumerate(product_list):
    print(v)
print(str(analytics).replace(', ', '\n '))
