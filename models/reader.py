class Reader:
    def __init__(self, first_name, last_name, ticket_number):
        self.first_name = first_name
        self.last_name = last_name
        self.ticket_number = ticket_number
        self.borrowed_books = []  # List of borrowed books

    def borrow_book(self, book):
        if book.borrow():
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books]) or "No books"
        return f"{self.first_name} {self.last_name} (#{self.ticket_number}) - Borrowed: {borrowed_titles}"

    def apply_borrowed_books(self, books):
        self.borrowed_books = [book for book in books if book]
        return self