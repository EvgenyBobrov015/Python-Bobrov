import re

slovar = dict()
with open("text_6.txt", "r", encoding="utf-8") as my_file:
    for i in my_file.readlines():
        slovar[i.split(":")[0]] = sum(map(int, re.findall(r'\d+', i)))
print(slovar)
