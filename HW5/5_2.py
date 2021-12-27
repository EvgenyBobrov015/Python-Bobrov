my_file = open("my_file2.txt", "r", encoding="utf-8")
content = my_file.read().split("\n")
for i, v in enumerate(content, 1):
    print(f"{i} строка - количество слов: {len(v.split())}")
print(f"Количество строк в файле: {len(content)}")
my_file.close()
