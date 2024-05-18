class Library:
    def __init__(self):
        """Инициализация объекта библиотеки с пустым списком книг."""
        self.book_list = []

    def add_book(self, book):
        """Добавляет книгу в список книг."""
        self.book_list.append(book)
        print(f"Книга '{book}' успешно добавлена в библиотеку.")

    def remove_book(self, book):
        """Удаляет книгу из списка книг."""
        if book in self.book_list:
            self.book_list.remove(book)
            print(f"Книга '{book}' успешно удалена из библиотеки.")
        else:
            print(f"Книги '{book}' нет в библиотеке.")

    def find_book(self, title):
        """Ищет книгу в списке книг по названию."""
        found_books = [book for book in self.book_list if book.get_title() == title]
        if found_books:
            print(f"Найдены следующие книги с названием '{title}':")
            for book in found_books:
                print(f"- {book}")
        else:
            print(f"Книги с названием '{title}' не найдены в библиотеке.")

class Book:
    def __init__(self, title, author):
        """Инициализация объекта книги с названием и автором."""
        self.title = title
        self.author = author

    def get_title(self):
        """Метод для получения названия книги."""
        return self.title

    def __str__(self):
        """Метод для представления объекта книги в виде строки."""
        return f"{self.title} (автор: {self.author})"

# Пример использования класса Library
if __name__ == "__main__":
    library = Library()

    book1 = Book("Война и мир", "Лев Толстой")
    book2 = Book("Преступление и наказание", "Федор Достоевский")
    library.add_book(book1)
    library.add_book(book2)

    library.find_book("Война и мир")
    library.find_book("Анна Каренина")

    library.remove_book(book1)
    library.find_book("Война и мир")
