import customtkinter as ctk
from tkinter import messagebox
from models.book import Book


class BookWindow:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Manage Books")

        # Поля ввода
        self.title_entry = ctk.CTkEntry(root, width=100)
        self.author_entry = ctk.CTkEntry(root, width=100)
        self.year_entry = ctk.CTkEntry(root, width=100)
        self.genre_entry = ctk.CTkEntry(root, width=100)
        self.copies_entry = ctk.CTkEntry(root, width=100)

        # Метки
        ctk.CTkLabel(root, text="Title:").grid(row=0, column=0)
        ctk.CTkLabel(root, text="Author:").grid(row=1, column=0)
        ctk.CTkLabel(root, text="Year:").grid(row=2, column=0)
        ctk.CTkLabel(root, text="Genre:").grid(row=3, column=0)
        ctk.CTkLabel(root, text="Copies:").grid(row=4, column=0)

        # Расположение полей
        self.title_entry.grid(row=0, pady=5, column=1)
        self.author_entry.grid(row=1, pady=5, column=1)
        self.year_entry.grid(row=2, pady=5, column=1)
        self.genre_entry.grid(row=3, pady=5, column=1)
        self.copies_entry.grid(row=4, pady=5, column=1)

        # Кнопки
        ctk.CTkButton(root, text="Add Book", command=self.add_book).grid(row=5, column=0, pady=5, padx=5)
        ctk.CTkButton(root, text="Delete Book", command=self.delete_book).grid(row=5, column=1, pady=5, padx=5)
        ctk.CTkButton(root, text="View Books",
                      command=self.view_books).grid(row=6, column=0, pady=5, padx=5, columnspan=2)

    def add_book(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        year = self.year_entry.get()
        genre = self.genre_entry.get()
        copies = self.copies_entry.get()

        if not (title and author and year and genre and copies):
            messagebox.showerror("Error", "All fields are required.")
            return

        try:
            book = Book(title, author, int(year), genre, int(copies))
            self.library.add_book(book)
            messagebox.showinfo("Success", "Book added successfully.")
        except ValueError:
            messagebox.showerror("Error", "Year and Copies must be integers.")

    def delete_book(self):
        """Удаляет книгу по названию."""
        title = self.title_entry.get().strip()

        if not title:
            messagebox.showerror("Error", "Please enter a book title.")
            return

        # Поиск книги
        books = [book for book in self.library.books if book.title.lower() == title.lower()]

        if not books:
            messagebox.showerror("Error", "Book with this title not found.")
            return

        # Удаление книги
        book_to_remove = books[0]  # В списке будет только один элемент
        self.library.books.remove(book_to_remove)
        self.library.save_data()
        messagebox.showinfo("Success", f"Book '{book_to_remove.title}' has been removed.")
        self.title_entry.delete(0, ctk.END)

    def view_books(self):
        books = self.library.books
        if books:
            book_list = "\n".join(str(book) for book in books)
            messagebox.showinfo("Books", book_list)
        else:
            messagebox.showinfo("Books", "No books available.")
