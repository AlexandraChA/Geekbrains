from abc import ABC, abstractmethod

class AbstractCloth(ABC):
    @property
    @abstractmethod
    def calc_tissue(self):
        pass

class Clothes(AbstractCloth):
    _clothes = []
    def __init__(self, name, size):
        self._name = name
        self.size = size
        self._clothes.append(self)
    @property
    def total_tissue(self):
        return sum(cloth.calc_tissue for cloth in self._clothes)

class Coat(Clothes):
    @property
    def calc_tissue(self):
        return (self.size/6.5 + 0.5)
    def __str__(self):
        return f'Для пальто {self._name} размером {self.size} нужно {self.calc_tissue} ткани.'

class Suit(Clothes):
    @property
    def calc_tissue(self):
        return (2*self.size + 0.3)
    def __str__(self):
        return f'Для костюма {self._name} для роста {self.size} нужно {self.calc_tissue} ткани.'


coat = Coat('Coat1', 3)
print(coat)
suit = Suit('Suit1', 165)
print(suit)
print(suit.total_tissue, coat.total_tissue)