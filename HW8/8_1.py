class Date:
    def __init__(self, date):
        self.date = date
        self.date_int(date)

    @classmethod
    def date_int(cls, date_string):
        date_string = date_string.split("-")
        if len(date_string) > 3:
            print("Данные некорретны!")
        else:
            try:
                for i, v in enumerate(date_string):
                    v = int(v)
                    date_string[i] = v
            except ValueError:
                print("Данные некорректны")
            else:
                return cls.validation(date_string)

    @staticmethod
    def validation(n):
        if n[0] > 30:
            n[0] = 30
        elif n[0] < 1:
            n[0] = 1
        if n[1] > 12:
            n[1] = 12
        elif n[1] < 1:
            n[1] = 1
        if n[2] > 2022:
            n[2] = 2022
        elif n[2] < 2000:
            n[2] = 2000
        print(f"{n[0]:02}.{n[1]:02}.{n[2]}")

date_1 = "9-10-1999"
date_2 = "neponytno-chto"
date_3 = "20-04-2011"

Date(date_1)
Date(date_2)
Date(date_3)
