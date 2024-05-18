import re
from collections import Counter

def analyze_text(file_name):
    """Функция для анализа содержимого текстового файла."""
    with open(file_name, 'r', encoding='utf-8') as file:
        text = file.read()

    # Удаление пунктуации для анализа частоты слов
    words = re.findall(r'\b\w+\b', text.lower())
    word_count = Counter(words)

    # Анализ длин предложений
    sentences = re.split(r'[.!?]', text)
    sentence_lengths = [len(sentence.split()) for sentence in sentences if sentence.strip()]

    # Подсчет предложений и слов
    num_sentences = len(sentences)
    num_words = len(words)

    # Ключевые слова для анализа
    keywords = ['python', 'programming', 'language']
    keyword_count = {keyword: words.count(keyword) for keyword in keywords}

    return {
        'word_count': word_count,
        'sentence_lengths': sentence_lengths,
        'num_sentences': num_sentences,
        'num_words': num_words,
        'keyword_count': keyword_count
    }

def display_statistics(stats):
    """Функция для отображения статистики анализа текста."""
    print("Общая статистика:")
    print(f"Количество предложений: {stats['num_sentences']}")
    print(f"Количество слов: {stats['num_words']}")
    
    print("\nЧастота слов:")
    for word, count in stats['word_count'].most_common(10):
        print(f"{word}: {count}")

    print("\nДлина предложений (в словах):")
    for length in stats['sentence_lengths']:
        print(length)

    print("\nКлючевые слова:")
    for keyword, count in stats['keyword_count'].items():
        print(f"{keyword}: {count}")

if __name__ == "__main__":
    file_name = "large_text.txt"
    stats = analyze_text(file_name)
    display_statistics(stats)
