import tkinter as tk
from tkinter import messagebox

from gui.book_window import BookWindow
from gui.reader_window import ReaderWindow
from gui.report_window import ReportWindow
from gui.borrow_return_window import BorrowReturnWindow

class MainWindow:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Library Management System")

        # Загрузка данных
        self.show_load_message()

        # Кнопки
        tk.Button(root, text="Manage Books", command=self.open_books_window).pack(pady=5)
        tk.Button(root, text="Manage Readers", command=self.open_readers_window).pack(pady=5)
        tk.Button(root, text="Borrow/Return Books", command=self.open_borrow_return_window).pack(pady=10)
        tk.Button(root, text="Reports", command=self.open_reports_window).pack(pady=5)
        tk.Button(root, text="Save Data", command=self.save_data).pack(pady=5)
        tk.Button(root, text="Exit", command=self.root.quit).pack(pady=5)

    def open_books_window(self):
        new_window = tk.Toplevel(self.root)
        BookWindow(new_window, self.library)

    def open_readers_window(self):
        new_window = tk.Toplevel(self.root)
        ReaderWindow(new_window, self.library)

    def open_reports_window(self):
        new_window = tk.Toplevel(self.root)
        ReportWindow(new_window, self.library)

    def open_borrow_return_window(self):
        new_window = tk.Toplevel(self.root)
        BorrowReturnWindow(new_window, self.library)

    def show_load_message(self):
        messagebox.showinfo("Welcome", "Data loaded from the last session successfully.")

    def save_data(self):
        self.library.save_data()
        messagebox.showinfo("Success", "Data saved successfully!")