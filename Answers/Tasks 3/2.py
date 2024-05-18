import csv

def read_csv(file_name):
    """Функция для чтения содержимого CSV-файла и вывода его на экран."""
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            print("Содержимое CSV-файла:")
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")

# Сохраняем данные в CSV-файл "data.csv"
data = [
    ["Иван", "Иванов", 25],
    ["Петр", "Петров", 30],
    ["Мария", "Сидорова", 28]
]

with open("data.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Имя", "Фамилия", "Возраст"])
    writer.writerows(data)

# Вызываем функцию для файла "data.csv"
read_csv("data.csv")
