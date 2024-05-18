import csv
import os
from collections import defaultdict

def analyze_directory(directory):
    age_stats = defaultdict(list)
    gender_stats = defaultdict(int)
    location_stats = defaultdict(int)
    all_data = []

    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            filepath = os.path.join(directory, filename)
            with open(filepath, 'r', newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    name = row.get('Имя')
                    age = row.get('Возраст')
                    gender = row.get('Пол')
                    location = row.get('Местоположение') or row.get('Город')

                    if age:
                        age_stats[age].append(name)
                    if gender:
                        gender_stats[gender] += 1
                    if location:
                        location_stats[location] += 1

                    all_data.append(row)

    return age_stats, gender_stats, location_stats, all_data

def display_statistics(age_stats, gender_stats, location_stats):
    print("Статистика по возрасту:")
    for age, users in age_stats.items():
        print(f"Возраст {age}: {len(users)} пользователей")

    print("\nСтатистика по полу:")
    for gender, count in gender_stats.items():
        print(f"Пол {gender}: {count} пользователей")

    print("\nСтатистика по местоположению:")
    for location, count in location_stats.items():
        print(f"Местоположение {location}: {count} пользователей")

def filter_data(all_data, age=None, location=None):
    filtered_data = all_data
    if age is not None:
        filtered_data = [user for user in filtered_data if user.get('Возраст') == age]
    if location is not None:
        filtered_data = [user for user in filtered_data if user.get('Местоположение') == location or user.get('Город') == location]
    
    return filtered_data

def display_filtered_data(filtered_data):
    print(f"\nФильтрованные данные ({len(filtered_data)} пользователей):")
    for user in filtered_data:
        print(user)

if __name__ == "__main__":
    directory = "data"
    age_stats, gender_stats, location_stats, all_data = analyze_directory(directory)
    
    display_statistics(age_stats, gender_stats, location_stats)
    
    age_filter = "25"
    location_filter = "Москва"
    filtered_data = filter_data(all_data, age=age_filter, location=location_filter)
    
    display_filtered_data(filtered_data)
