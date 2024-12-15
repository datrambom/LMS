import json
import os

from models.book import Book
from models.reader import Reader


class FileManager:
    def __init__(self, books_file="data/books.json", readers_file="data/readers.json"):
        self.books_file = books_file
        self.readers_file = readers_file
        self._ensure_file(self.books_file)
        self._ensure_file(self.readers_file)

    def _ensure_file(self, file_path):
        """Создаёт пустой файл, если его не существует."""
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                json.dump([], file)

    def save_books(self, books):
        """Сохраняет список книг в файл."""
        with open(self.books_file, 'w') as file:
            json.dump([book.__dict__ for book in books], file, indent=4)

    def load_books(self):
        """Загружает список книг из файла."""
        with open(self.books_file, 'r') as file:
            books_data = json.load(file)
        return [
            Book(
                title=book['title'],
                author=book['author'],
                year=book['year'],
                genre=book['genre'],
                copies=book['copies']
            ) for book in books_data
        ]

    def save_readers(self, readers):
        """Сохраняет список читателей в файл."""
        with open(self.readers_file, 'w') as file:
            json.dump([{
                'first_name': reader.first_name,
                'last_name': reader.last_name,
                'ticket_number': reader.ticket_number,
                'borrowed_books': [book.title for book in reader.borrowed_books]
            } for reader in readers], file, indent=4)

    def load_readers(self, books):
        """Загружает список читателей из файла."""
        with open(self.readers_file, 'r') as file:
            readers_data = json.load(file)
        return [
            Reader(
                first_name=reader['first_name'],
                last_name=reader['last_name'],
                ticket_number=reader['ticket_number'],
            ).apply_borrowed_books(
                books=[next((book for book in books if book.title == book_title), None) for book_title in reader['borrowed_books']]
            ) for reader in readers_data
        ]
