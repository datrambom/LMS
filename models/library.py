from utils.file_manager import FileManager


class Library:
    def __init__(self):
        self.file_manager = FileManager()
        self.books = self.file_manager.load_books()  # List of all books
        self.readers = self.file_manager.load_readers(self.books)  # List of all readers

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def find_book(self, title=None):
        return next((book for book in self.books if book.title == title), None)

    def add_reader(self, reader):
        self.readers.append(reader)
        self.save_data()

    def find_reader(self, ticket_number=None):
        return next((reader for reader in self.readers if reader.ticket_number == ticket_number), None)

    def borrow_book(self, ticket_number, book_title):
        reader = self.find_reader(ticket_number)
        book = self.find_book(book_title)
        if reader and book:
            if reader.borrow_book(book):
                return f"'{book.title}' has been borrowed by {reader.first_name} {reader.last_name}."
            return f"No copies of '{book.title}' available."
        self.save_data()
        return "Book or Reader not found."

    def return_book(self, ticket_number, book_title):
        reader = self.find_reader(ticket_number)
        book = self.find_book(book_title)
        if reader and book:
            if reader.return_book(book):
                return f"'{book.title}' has been returned by {reader.first_name} {reader.last_name}."
            return f"{reader.first_name} {reader.last_name} has not borrowed '{book.title}'."
        self.save_data()
        return "Book or Reader not found."

    def save_data(self):
        #Сохраняет данные в JSON-файлы
        self.file_manager.save_books(self.books)
        self.file_manager.save_readers(self.readers)

    def report_borrowed_in_store(self):
        #Возвращает отчёт о выданных и оставшихся экземплярах книг
        report = []
        for book in self.books:
            borrowed = sum(
                1 for reader in self.readers for b in reader.borrowed_books if b.title == book.title
            )
            report.append(f"'{book.title}' - Borrowed: {borrowed}, In Store: {book.copies}")
        return "\n".join(report)
