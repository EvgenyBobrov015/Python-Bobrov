from random import randint


class Car:
    def __init__(self, name, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def go(self):
        print(f"Автомобиль {self.name} начал движение.")

    def stop(self):
        print(f"Автомобиль {self.name} остановился.")

    def turn(self):
        print(f"Автомобиль {self.name} повернул направо.") if randint(0, 1) == 0 else print(
            f"Автомобиль {self.name} повернул налево.")

    def show_speed(self):
        print(f"Скорость автомобиля {self.name} : {self.speed}")


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на: {self.speed - 60} км/ч")
        else:
            super().show_speed()


class SportCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Превышение скорости на: {self.speed - 60} км/ч")
        else:
            super().show_speed()


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Превышение скорости на: {self.speed - 40} км/ч")
        else:
            super().show_speed()


class PoliceCar(Car):
    pass


town_car = TownCar("Toyota Corolla", 70, "Черный", False)
sport_car = SportCar("Porche Panamera", 55, "Синий", False)
work_car = WorkCar("VW Transporter", 40, "Коричневый", False)
police_car = PoliceCar("Shkoda Octavia", 100, "белый", True)

cars = [town_car, sport_car, work_car, police_car]

for i in cars:
    i.go()
    i.show_speed()
    i.turn()
    i.stop()
    print()
