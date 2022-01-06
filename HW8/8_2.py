class NotZeroEx(Exception):
    def __init__(self, zero):
        self.zero = zero

    def __str__(self):
        return f"You're trying to break the universe!!!"


class Division:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def div(self):
        if self.b == 0:
            raise NotZeroEx(self.b)
        print(self.a / self.b)


div_1 = Division(int(input("Var1: ")), int(input("Var2: ")))
try:
    div_1.div()
except NotZeroEx:
    print("You're trying to break the universe!!!")
