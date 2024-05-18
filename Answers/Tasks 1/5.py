import csv

def read_csv(file_path):
    """Считывает данные из CSV файла и возвращает их в виде списка списков."""
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        data = [list(map(float, row)) for row in reader]
    return data

def calculate_column_averages(data):
    """Вычисляет среднее арифметическое чисел в каждой колонке."""
    if not data:
        return []

    num_columns = len(data[0])
    column_sums = [0] * num_columns
    column_counts = [0] * num_columns

    for row in data:
        for i in range(num_columns):
            column_sums[i] += row[i]
            column_counts[i] += 1

    column_averages = [column_sums[i] / column_counts[i] for i in range(num_columns)]
    return column_averages

def main():
    file_path = 'data.csv'
    data = read_csv(file_path)
    averages = calculate_column_averages(data)
    print("Среднее арифметическое чисел в каждой колонке:")
    for i, avg in enumerate(averages):
        print(f"Колонка {i + 1}: {avg:.2f}")

if __name__ == "__main__":
    main()
