class Matrix:
    def __init__(self, rows):
        self.rows = rows
        self.num_rows = len(rows)
        self.num_cols = len(rows[0])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.rows])

    def __add__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Матрицы разных размеров нельзя сложить")
        result = [[self.rows[i][j] + other.rows[i][j] for j in range(self.num_cols)] for i in range(self.num_rows)]
        return Matrix(result)

    def __sub__(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Матрицы разных размеров нельзя вычитать")
        result = [[self.rows[i][j] - other.rows[i][j] for j in range(self.num_cols)] for i in range(self.num_rows)]
        return Matrix(result)

    def __mul__(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Невозможно умножить матрицы: неправильные размеры")
        result = [[sum(self.rows[i][k] * other.rows[k][j] for k in range(self.num_cols)) 
                   for j in range(other.num_cols)] for i in range(self.num_rows)]
        return Matrix(result)

    def transpose(self):
        transposed = [[self.rows[j][i] for j in range(self.num_rows)] for i in range(self.num_cols)]
        return Matrix(transposed)

    def determinant(self):
        if self.num_rows != self.num_cols:
            raise ValueError("Матрица должна быть квадратной для вычисления определителя")
        if self.num_rows == 1:
            return self.rows[0][0]
        if self.num_rows == 2:
            return self.rows[0][0] * self.rows[1][1] - self.rows[0][1] * self.rows[1][0]
        det = 0
        for j in range(self.num_cols):
            minor = [row[:j] + row[j+1:] for row in (self.rows[1:])]
            det += (-1) ** j * self.rows[0][j] * Matrix(minor).determinant()
        return det

# Пример
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8, 9], [10, 11, 12]])

print("Матрица 1:")
print(matrix1)

print("\nМатрица 2:")
print(matrix2)

print("\nСложение:")
print(matrix1 + matrix2)

print("\nВычитание:")
print(matrix1 - matrix2)

print("\nУмножение:")
print(matrix1 * matrix2)

print("\nТранспонирование матрицы 1:")
print(matrix1.transpose())

print("\nОпределитель матрицы 1:")
print(matrix1.determinant())
