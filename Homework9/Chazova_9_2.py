
class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
    def calc_mass(self, mass, thickness):
        return self._width * self._length * mass * thickness

try:
    road = Road(5000, 20)
    print(road.calc_mass(25, 5))
except TypeError:
    msg = 'Оба объекта требуют по два аргумента.'
    raise TypeError(msg)
