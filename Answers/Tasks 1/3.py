import string

def is_palindrome(s):
    """Проверка, является ли строка палиндромом."""
    s = ''.join(char.lower() for char in s if char.isalnum())
    return s == s[::-1]

input_string = input("Введите строку: ")

if is_palindrome(input_string):
    print("Строка является палиндромом.")
else:
    print("Строка не является палиндромом.")
