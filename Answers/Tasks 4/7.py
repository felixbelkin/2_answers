import csv
from collections import defaultdict

def calculate_statistics(file_name):
    statistics = defaultdict(list)

    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)
        for row in reader:
            for i, value in enumerate(row):
                statistics[headers[i]].append(value)

    return statistics

def print_statistics(statistics):
    for column, data in statistics.items():
        print(f"Столбец '{column}':")
        print("Среднее значение:", sum(map(float, data)) / len(data))
        print("Минимальное значение:", min(map(float, data)))
        print("Максимальное значение:", max(map(float, data)))
        print("Общее количество значений:", len(data))
        print()

file_name = 'data.csv'
statistics = calculate_statistics(file_name)
print_statistics(statistics)
