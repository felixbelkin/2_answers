class Book:
    def __init__(self, title, author):
        """Инициализация объекта книги с названием и автором."""
        self._title = title
        self._author = author

    def get_title(self):
        """Метод для получения названия книги."""
        return self._title

    def get_author(self):
        """Метод для получения автора книги."""
        return self._author

if __name__ == "__main__":
    book = Book("Война и мир", "Лев Толстой")
    print(f"Название: {book.get_title()}")
    print(f"Автор: {book.get_author()}")
