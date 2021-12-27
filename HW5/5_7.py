import json


firm_dict = dict()
average_profit = dict()
with open("text_7.txt", "r", encoding="utf-8") as my_file:
    for i in my_file.readlines():
        firm_dict[i.split()[0]] = int(i.split()[2]) - int(i.split()[3])
    profit_list = [n for n in firm_dict.values() if n > 0]
    average_profit["average_profit"] = sum(profit_list) / len(profit_list)
    my_list = [firm_dict, average_profit]
with open("my_file7.json", "w", encoding="utf-8") as my_file7:
    json.dump(my_list, my_file7, ensure_ascii=False, indent=4)
