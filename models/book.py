class Book:
    def __init__(self, title, author, year, genre, copies):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.copies = copies

    def borrow(self):
        if self.copies > 0:
            self.copies -= 1
            return True
        return False

    def return_book(self):
        self.copies += 1

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.genre}, Copies: {self.copies}"
