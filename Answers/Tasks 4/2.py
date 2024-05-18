import re
from collections import Counter

def read_file(file_name):
    """Читает содержимое текстового файла."""
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def clean_text(text):
    """Очищает текст от пунктуации и приводит его к нижнему регистру."""
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def get_word_frequencies(text):
    """Возвращает частоту слов в тексте."""
    words = text.split()
    word_count = Counter(words)
    return word_count

def print_top_words(word_count, top_n=10):
    """Выводит наиболее часто встречающиеся слова."""
    most_common_words = word_count.most_common(top_n)
    print(f"Топ {top_n} наиболее часто встречающихся слов:")
    for word, count in most_common_words:
        print(f"{word}: {count}")

if __name__ == "__main__":
    file_name = "example.txt"
    text = read_file(file_name)
    cleaned_text = clean_text(text)
    word_count = get_word_frequencies(cleaned_text)
    print_top_words(word_count, top_n=10)
