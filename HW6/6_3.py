class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": w, "bonus": b}


class Position(Worker):
    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return sum(self._income.values())


ivanov = Position("Ivan", "Ivanov", "seller", 20000, 5000)
print(ivanov.get_full_name())
print(ivanov.get_total_income())
