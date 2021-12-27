my_dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
with open("text_4.txt", "r", encoding="utf-8") as my_file:
    content = my_file.read().split("\n")
    with open("text_4.1.txt", "w", encoding="utf-8") as new_file:
        for i in content:
            for j in my_dict:
                i = i.replace(j, my_dict[j])
            new_file.write(f"{i}\n")
            print(i)
