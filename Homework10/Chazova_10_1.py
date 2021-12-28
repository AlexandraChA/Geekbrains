class Matrix:
    def __init__(self, numbers):
        self.__numb =  numbers
        row = len(self.__numb)
        col = len(self.__numb[1])
        self.__size = [row, col]

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__numb])

    def __add__(self, other):
        if self.__size != other.__size:
            msg = 'У матриц разная размерность, их нельзя сложить.'
            raise ValueError(msg)
        else:
            result = self.__numb
            for i in range(len(self.__numb)):
                for j in range(len(self.__numb[1])):
                    result[i][j] += other.__numb[i][j]
        return Matrix(result)

matr = Matrix([[1,2],[3,5]])
print(matr)
matr2 = Matrix([[2,3],[7,8]])
print(matr2)

print(matr+matr2)

