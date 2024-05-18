import math

class Point:
    def __init__(self, x, y):
        """Инициализация объекта точки с координатами x и y."""
        self.x = x
        self.y = y

    def distance_to(self, other_point):
        """Вычисление расстояния между двумя точками."""
        distance = math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)
        return distance

    def move(self, distance, direction):
        """Перемещение точки на заданное расстояние в заданном направлении."""
        if direction == 'вверх':
            self.y += distance
        elif direction == 'вниз':
            self.y -= distance
        elif direction == 'влево':
            self.x -= distance
        elif direction == 'вправо':
            self.x += distance
        else:
            print("Некорректное направление. Допустимые значения: 'вверх', 'вниз', 'влево', 'вправо'.")

    def is_on_x_axis(self):
        """Проверка, лежит ли точка на оси x."""
        return self.y == 0

    def is_on_y_axis(self):
        """Проверка, лежит ли точка на оси y."""
        return self.x == 0

# Пример
if __name__ == "__main__":
    point1 = Point(3, 4)
    point2 = Point(-2, 0)

    distance = point1.distance_to(point2)
    print(f"Расстояние между точками: {distance:.2f}")

    point1.move(5, 'вправо')
    print(f"Новые координаты точки 1: ({point1.x}, {point1.y})")

    print(f"Точка 1 лежит на оси x: {point1.is_on_x_axis()}")
    print(f"Точка 2 лежит на оси y: {point2.is_on_y_axis()}")
