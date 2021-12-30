class Road:
    def __init__(self, a, b):
        self._lenght = int(a)
        self._width = int(b)

    def mass(self):
        m = (self._lenght * self._width * 125) / 1000
        print(f"Требуемая масса асфальта: {m} т.")


road_1 = Road(input("Введите длину дороги (м): "), input("Введите ширину дороги (м): "))
road_1.mass()
