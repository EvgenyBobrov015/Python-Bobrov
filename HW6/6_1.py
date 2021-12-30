import time


class TrafficLight:
    __color = {"red": 7, "yellow": 3, "green": 3}

    def running(self):
        for k in self.__color:
            print(f"\r{k}", end="")
            time.sleep(self.__color[k])


a = TrafficLight()
a.running()
