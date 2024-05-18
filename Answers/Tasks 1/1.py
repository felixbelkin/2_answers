input_string = input("Введите строку: ")
words = input_string.lower().split()
unique_words = set(words)
sorted_unique_words = sorted(unique_words)

print("Уникальные слова в алфавитном порядке:")
for word in sorted_unique_words:
    print(word)
