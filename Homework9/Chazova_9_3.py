
class Worker:
    def __init__(self, name, surname, position, wage, bonus = 0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])
    def get_total_income(self):
        return sum(self._income.values())
try:
    pers1 = Position('Ivan', 'Ivanov', 'worker', 20000, 5000)
    print(pers1.name, pers1.surname, pers1.position)
    print(pers1.get_full_name(), pers1.get_total_income())
except TypeError:
    msg = 'Объект класса Position и Worker требует минимум 4 аргумента (дополнительно бонус).'
    raise TypeError(msg)