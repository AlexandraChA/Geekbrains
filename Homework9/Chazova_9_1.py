from time import sleep

class TrafficLight:
    def __init__(self, color):
        self.__color = color
    def running(self):
        for key, value in self.__color.items():
            sleep(value)
            print(key)

lights = TrafficLight({'Red':7, 'Yellow': 2, 'Green': 7})
lights.running()
