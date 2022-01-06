class Comp:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = f"{a}+{b}j"

    def __add__(self, other):
        i = self.a + other.a
        j = self.b + other.b
        return f"{i}+{j}j" if j >= 0 else f"{i}{j}j"

    def __mul__(self, other):
        n = self.a * other.a - self.b * other.b
        k = (self.a * other.b + self.b * other.a) * -1
        return f"{n}+{k}j" if k >= 0 else f"{n}{k}j"


comp_1 = Comp(1, 2)
comp_2 = Comp(2, 4)
print(comp_1 + comp_2)
print(comp_1 * comp_2)
