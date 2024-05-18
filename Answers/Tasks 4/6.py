class LinearEquationSolver:
    def __init__(self):
        pass

    def solve(self, coefficients, constants):
        if len(coefficients) != len(constants):
            print("Некорректные входные данные.")
            return None

        n = len(coefficients)
        
        for i in range(n):
            max_row = i
            for j in range(i+1, n):
                if abs(coefficients[j][i]) > abs(coefficients[max_row][i]):
                    max_row = j
            coefficients[i], coefficients[max_row] = coefficients[max_row], coefficients[i]
            constants[i], constants[max_row] = constants[max_row], constants[i]
            for j in range(i+1, n):
                ratio = coefficients[j][i] / coefficients[i][i]
                for k in range(i, n):
                    coefficients[j][k] -= ratio * coefficients[i][k]
                constants[j] -= ratio * constants[i]
        solution = [0] * n
        for i in range(n-1, -1, -1):
            solution[i] = constants[i] / coefficients[i][i]
            for j in range(i):
                constants[j] -= coefficients[j][i] * solution[i]
        return solution

solver = LinearEquationSolver()
coefficients = [[2, 3],
                [4, -1]]
constants = [7, 5]
solution = solver.solve(coefficients, constants)
print("Решение системы уравнений:", solution)
