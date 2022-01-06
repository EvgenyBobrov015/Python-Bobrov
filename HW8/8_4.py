class Store:
    max_count = 100
    dict_inv = {}

    def __init__(self, count):
        self.count = count

    def in_dict(self):
        return self.dict_inv | self.count


class OffAppl:
    create = {}

    def __init__(self, model, price, lot):
        self.model = model
        self.price = price
        self.lot = lot

    def in_store(self, index, num):
        if num > self.create[index]:
            print("Столько товара не создано!")
        elif num == 0:
            x = self.create[index]
            del self.create[index]
            return Store(x)
        else:
            x = self.create
            x[index] = num
            self.create[index] -= num
            return Store(x[index])


class Print(OffAppl):
    def __init__(self, model, price, lot, printer):
        super().__init__(model, price, lot)
        self.printer = printer

    def build(self):
        self.create[(self.printer, self.model, self.price)] = self.price


class Scan(OffAppl):
    def __init__(self, model, price, lot, scaner):
        super().__init__(model, price, lot)
        self.scaner = scaner

    def build(self):
        self.create[(self.scaner, self.model, self.price)] = self.price


class Xer(OffAppl):
    def __init__(self, model, price, lot, xerox):
        super().__init__(model, price, lot)
        self.xerox = xerox

    def build(self):
        self.create[(self.xerox, self.model, self.price)] = self.price


q = 0
while q != "quit":
    a = int(input("Какой товар создать?\n1 - Принтер\n2 - Сканер\n3 - Ксерокс\n"))
    b = input("Введите название модели: ")
    c = input("Введите цену: ")
    d = input("Введите количество: ")
    if a == 1:
        e = "Принтер"
        f = Print(b, c, d, e)
        f.build()
    elif a == 2:
        e = "Сканер"
        f = Scan(b, c, d, e)
        f.build()
    elif a == 3:
        e = "Ксерокс"
        f = Xer(b, c, d, e)
        f.build()
    else:
        print("Введены неверные данные!")
    q = input("Для выхода из меню создания введите 'quit', для добовления товара нажмите 'Enter'")
