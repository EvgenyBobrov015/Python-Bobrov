class Stationary:
    def __init__(self, title="Нарисуем слона!"):
        self.title = title

    def draw(self):
        print(f"{self.title} Осталось выбрать чем?!.")


class Pen(Stationary):
    def draw(self):
        print(f"{self.title} Ручкой!")


class Pencil(Stationary):
    def draw(self):
        print(f"{self.title} Карандашом!")


class Handle(Stationary):
    def draw(self):
        print(f"{self.title} Маркером!")


t = Stationary()
pen = Pen()
pencil = Pencil()
handle = Handle()

n = [t, pen, pencil, handle]
for i in n:
    i.draw()
    print()
