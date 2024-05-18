def read_file(file_name):
    """Функция для чтения содержимого файла и вывода его на экран."""
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")

with open("example.txt", 'w') as file:
    file.write("Это первая строка текста.\n")
    file.write("Это вторая строка текста.\n")
    file.write("Это третья строка текста.\n")

# answer
read_file("example.txt")