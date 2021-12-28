class Cell:
    def __init__(self, numb):
        self._numb = numb
    def __str__(self):
        return f'В клетке находится {self._numb} ячеек.'
    def __add__(self, other):
        return Cell(self._numb+ other._numb)
    def __sub__(self, other):
        if self._numb < other._numb:
            msg = 'Разность клеток меньше нуля.'
            raise ValueError(msg)
        else:
            return Cell(self._numb-other._numb)
    def __mul__(self, other):
        return Cell(self._numb*other._numb)
    def __truediv__(self, other):
        return Cell(self._numb//other._numb)
    def make_order(self, row):
        n_rows = self._numb//row
        left = self._numb%row
        return '\n'.join(['*'*row]*n_rows+['*'*left])

c1 = Cell(27)
c2 = Cell(11)
print(c1, c2)
print(c1+c2)
print(c1*c2)
print(c1-c2)
print(c1/c2)
print(c1.make_order(13))
c3 = Cell(15)
print(c3.make_order(5))

print(c2 - c1)