class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой: {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом: {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером: {self.title}')

pen = Pen('надпись')
pen.draw()
pencil = Pencil('надпись')
pencil.draw()
handle = Handle('надпись')
handle.draw()