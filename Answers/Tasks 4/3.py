def power(a, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(a, -n)
    elif n % 2 == 0:
        half_power = power(a, n // 2)
        return half_power * half_power
    else:
        return a * power(a, n - 1)

# Пример 
base = 2
exponent = 10
result = power(base, exponent)
print(f"{base}^{exponent} = {result}")
