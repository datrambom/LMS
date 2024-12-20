from tkinter import messagebox
import customtkinter as tk


#from tkinter.scrolledtext import ScrolledText


class ReportWindow:
    def __init__(self, root, library):
        self.report_text = None
        self.root = root
        self.library = library
        self.root.title("Reports")

        #self.report_text = ScrolledText(root, width=50, height=20)
        #self.report_text.pack(pady=10)

        # Кнопки
        tk.CTkButton(root, text="Books by Genre", command=self.report_books_by_genre).pack(pady=5, padx=5)
        tk.CTkButton(root, text="Total Books", command=self.report_total_books).pack(pady=5, padx=5)
        tk.CTkButton(root, text="Reader Report", command=self.report_reader_books).pack(pady=5, padx=5)
        tk.CTkButton(root, text="Borrowed/In Store", command=self.show_borrowed_in_store).pack(pady=5, padx=5)
        tk.CTkButton(root, text="Close", command=self.root.destroy).pack(pady=5, padx=5)

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

    def show_borrowed_in_store(self):
        report = self.library.report_borrowed_in_store()  # Генерация отчёта из библиотеки
        if not report:
            report = "No books available in the library at the moment."  # Обработка пустого отчёта
        messagebox.showinfo("Borrowed/In Store Report", report)
