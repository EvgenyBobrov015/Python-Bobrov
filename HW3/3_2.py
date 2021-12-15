def my_func(name=input("Name: "), surname=input("Surname: "), years=input("Years of brith: "), city=input("City: "),
            e_mail=input("E-mail: "), phone=input("Phone number: ")):
    user = [name, surname, years, city, e_mail, phone]
    return user


print(" ".join(my_func()))
