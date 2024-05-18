def is_prime(n):
    """Проверка, является ли число простым."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def sum_of_primes(a, b):
    """Вычисление суммы простых чисел в интервале [a, b]."""
    total = 0
    for num in range(a, b + 1):
        if is_prime(num):
            total += num
    return total

# Запрашиваем у пользователя значения a и b
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

# Находим и выводим сумму всех простых чисел в заданном интервале
result = sum_of_primes(a, b)
print(f"Сумма всех простых чисел в интервале от {a} до {b} равна {result}")
