class TriangleChecker:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def is_triangle(self):
        """Проверяет, можно ли из заданных отрезков построить треугольник."""
        if not all(isinstance(x, (int, float)) for x in [self.a, self.b, self.c]):
            return "Нужно вводить только числа !"
        if any(x <= 0 for x in [self.a, self.b, self.c]):
            return "С отрицательными числами ничего не выйдет !"
        if (self.a + self.b > self.c) and (self.a + self.c > self.b) and (self.b + self.c > self.a):
            return "Ура, можно построить треугольник !"
        else:
            return "Жаль, но из этого треугольник не сделать."
        
if __name__ == "__main__":
    examples = [
        (3, 4, 5),
        (-3, 4, 5),
        ("3", 4, 5),
        (1, 2, 10)
    ]

    for sides in examples:
        checker = TriangleChecker(*sides)
        result = checker.is_triangle()
        print(f"Отрезокк {sides}: {result}")
