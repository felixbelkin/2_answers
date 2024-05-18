import random

def generate_crossword(words):
    """
    Генерирует кроссворд на основе заданных слов.

    :param words: Список слов для использования в кроссворде.
    :return: Список строк, представляющих собой сгенерированный кроссворд.
    """
    # Находим максимальную длину слова
    max_length = max(len(word) for word in words)

    # Создаем пустой кроссворд
    crossword = [[' ' for _ in range(max_length)] for _ in range(max_length)]

    # Заполняем кроссворд словами
    for word in words:
        direction = random.choice(['horizontal', 'vertical'])
        if direction == 'horizontal':
            row = random.randint(0, max_length - 1)
            col = random.randint(0, max_length - len(word))
            for i, letter in enumerate(word):
                crossword[row][col + i] = letter
        else:
            row = random.randint(0, max_length - len(word))
            col = random.randint(0, max_length - 1)
            for i, letter in enumerate(word):
                crossword[row + i][col] = letter

    return [''.join(row) for row in crossword]

def solve_crossword(crossword):
    """
    Решает кроссворд.

    :param crossword: Список строк, представляющих собой кроссворд.
    :return: Список строк, представляющих собой решенный кроссворд.
    """
    # Простое решение - транспонирование кроссворда
    solved_crossword = [''.join(row) for row in zip(*crossword)]
    return solved_crossword

# Пример использования
words = ['python', 'crossword', 'puzzle', 'solution']
generated_crossword = generate_crossword(words)
print("Сгенерированный кроссворд:")
for row in generated_crossword:
    print(row)

solved_crossword = solve_crossword(generated_crossword)
print("\nРешенный кроссворд:")
for row in solved_crossword:
    print(row)
