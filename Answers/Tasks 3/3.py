import csv

def process_large_csv(file_name):
    """Функция для обработки данных из большого CSV-файла."""
    total_temperature = 0
    count_temperature = 0
    min_humidity = float('inf')
    max_humidity = float('-inf')

    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                # Пример обработки данных: вычисление среднего значения температуры
                temperature = float(row['Temperature'])
                total_temperature += temperature
                count_temperature += 1

                # Пример обработки данных: нахождение минимальной и максимальной влажности
                humidity = float(row['Humidity'])
                if humidity < min_humidity:
                    min_humidity = humidity
                if humidity > max_humidity:
                    max_humidity = humidity

        avg_temperature = total_temperature / count_temperature if count_temperature != 0 else 0

        print(f"Средняя температура: {avg_temperature}")
        print(f"Минимальная влажность: {min_humidity}")
        print(f"Максимальная влажность: {max_humidity}")

    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
    except KeyError as e:
        print(f"Отсутствует необходимый столбец в CSV-файле: {e}")
    except ValueError as e:
        print(f"Ошибка преобразования данных: {e}")

process_large_csv("large_data.csv")
