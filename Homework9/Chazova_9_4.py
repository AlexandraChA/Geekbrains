
class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
    def go(self):
        print('Машина поехала.')
    def stop(self):
        print('Машина остановилась')
    def turn(self, direction):
        print(f'Машина свернула {direction}')
    def show_speed(self):
        print(f'Скорость автомобиля равна {self.speed} км/ч')

class TownCar(Car):
    def show_speed(self):
        if self.speed <= 60:
            print(f'Скорость автомобиля равна {self.speed} км/ч')
        else:
            print(f'Снизьте скорость! Скорость автомобиля равна {self.speed} км/ч')

class WorkCar(Car):
    def show_speed(self):
        if self.speed <= 40:
            print(f'Скорость автомобиля равна {self.speed} км/ч')
        else:
            print(f'Снизьте скорость! Скорость автомобиля равна {self.speed} км/ч')

class SportCar(Car):
    pass

class PoliceCar(Car):
    def __init__(self, *args):
        super().__init__(*args, is_police=True)


try:
    car_town1 = TownCar(55, 'white', 'Reno')
    car_town1.show_speed()
    car_town2 = TownCar(70, 'white', 'Reno')
    car_town2.show_speed()
    work_town = WorkCar(55, 'white', 'Reno')
    work_town.show_speed()
    police = PoliceCar(80, 'black', 'Reno')
    police.show_speed()
except TypeError:
    msg = 'Объекты TownCar и WorkCar должны иметь три аргумента.'
    raise TypeError(msg)