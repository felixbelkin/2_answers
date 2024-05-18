import csv

def calculate_column_sum(file_name, column_index):
    total_sum = 0

    with open(file_name, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                value = float(row[column_index])
                total_sum += value
            except ValueError:
                pass

    return total_sum

# Пример
file_name = 'data.csv'
column_index = 1  
total_sum = calculate_column_sum(file_name, column_index)
print(f"Сумма числовых значений в столбце {column_index + 1}: {total_sum}")
