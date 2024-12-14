class Library:
    def __init__(self):
        self.file_manager = None
        self.books = []   # List of all books
        self.readers = []  # List of all readers

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title=None):
        return next((book for book in self.books if book.title == title), None)

    def add_reader(self, reader):
        self.readers.append(reader)

    def find_reader(self, ticket_number=None):
        return next((reader for reader in self.readers if reader.ticket_number == ticket_number), None)

    def borrow_book(self, ticket_number, book_title):
        reader = self.find_reader(ticket_number)
        book = self.find_book(book_title)
        if reader and book:
            if reader.borrow_book(book):
                return f"'{book.title}' has been borrowed by {reader.first_name} {reader.last_name}."
            return f"No copies of '{book.title}' available."
        return "Book or Reader not found."

    def return_book(self, ticket_number, book_title):
        reader = self.find_reader(ticket_number)
        book = self.find_book(book_title)
        if reader and book:
            if reader.return_book(book):
                return f"'{book.title}' has been returned by {reader.first_name} {reader.last_name}."
            return f"{reader.first_name} {reader.last_name} has not borrowed '{book.title}'."
        return "Book or Reader not found."

