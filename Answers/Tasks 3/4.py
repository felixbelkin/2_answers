import csv

def merge_csv_files(output_file, *input_files):
    """Функция для объединения данных из нескольких CSV-файлов в один."""
    fieldnames = ['Имя', 'Возраст', 'Местоположение']
    
    try:
        with open(output_file, 'w', newline='') as out_file:
            writer = csv.DictWriter(out_file, fieldnames=fieldnames)
            writer.writeheader()

            for file_name in input_files:
                try:
                    with open(file_name, 'r', newline='') as in_file:
                        reader = csv.DictReader(in_file)
                        
                        # Проверяем, соответствуют ли столбцы ожидаемому формату
                        if reader.fieldnames != fieldnames:
                            print(f"Предупреждение: формат файла '{file_name}' не соответствует ожидаемому формату.")
                            continue
                        
                        for row in reader:
                            writer.writerow(row)
                except FileNotFoundError:
                    print(f"Файл '{file_name}' не найден.")
                except KeyError as e:
                    print(f"Отсутствует необходимый столбец в CSV-файле '{file_name}': {e}")
                except ValueError as e:
                    print(f"Ошибка преобразования данных в файле '{file_name}': {e}")

        print(f"Данные успешно объединены и сохранены в файл '{output_file}'.")

    except IOError as e:
        print(f"Ошибка записи в файл '{output_file}': {e}")

# Пример
merge_csv_files("merged_data.csv", "data1.csv", "data2.csv", "data3.csv")
