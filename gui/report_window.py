import tkinter as tk
from tkinter import messagebox

class ReportWindow:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Reports")

        # Кнопки
        tk.Button(root, text="Books by Genre", command=self.report_books_by_genre).pack(pady=5)
        tk.Button(root, text="Total Books", command=self.report_total_books).pack(pady=5)
        tk.Button(root, text="Reader Report", command=self.report_reader_books).pack(pady=5)

    def report_books_by_genre(self):
        genre_report = {}
        for book in self.library.books:
            genre_report[book.genre] = genre_report.get(book.genre, 0) + book.copies
        report = "\n".join([f"{genre}: {count}" for genre, count in genre_report.items()])
        messagebox.showinfo("Books by Genre", report if report else "No books available.")

    def report_total_books(self):
        total_books = sum(book.copies for book in self.library.books)
        messagebox.showinfo("Total Books", f"Total books in library: {total_books}")

    def report_reader_books(self):
        readers = self.library.readers
        if not readers:
            messagebox.showinfo("Readers", "No readers available.")
            return

        report = "\n".join(
            f"{reader.first_name} {reader.last_name}: {', '.join([book.title for book in reader.borrowed_books]) or 'No books'}"
            for reader in readers
        )
        messagebox.showinfo("Reader Report", report)
