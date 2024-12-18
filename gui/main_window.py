import customtkinter as ctk
from tkinter import messagebox

from gui.book_window import BookWindow
from gui.reader_window import ReaderWindow
from gui.report_window import ReportWindow
from gui.borrow_return_window import BorrowReturnWindow

class MainWindow:
    def __init__(self, root, library):
        ctk.set_appearance_mode('system')
        ctk.set_default_color_theme('dark-blue')
        self.root = root
        self.library = library
        self.root.title("LMS")
        self.root.geometry("195x260")
        self.root.resizable(False, False)

        # Загрузка данных
        self.show_load_message()

        # Кнопки
        empty_space = ctk.CTkLabel(root, text="", height=1)
        empty_space.pack()
        ctk.CTkButton(root, text="Manage Books", command=self.open_books_window).pack(pady=5)
        ctk.CTkButton(root, text="Manage Readers", command=self.open_readers_window).pack(pady=5)
        ctk.CTkButton(root, text="Borrow/Return Books", command=self.open_borrow_return_window).pack(pady=5)
        ctk.CTkButton(root, text="Reports", command=self.open_reports_window).pack(pady=5)
        ctk.CTkButton(root, text="Save Data", command=self.save_data).pack(pady=5)
        ctk.CTkButton(root, text="Exit", command=self.root.quit).pack(pady=5)

    def open_books_window(self):
        new_window = ctk.CTkToplevel(self.root)
        BookWindow(new_window, self.library)

    def open_readers_window(self):
        new_window = ctk.CTkToplevel(self.root)
        ReaderWindow(new_window, self.library)

    def open_reports_window(self):
        new_window = ctk.CTkToplevel(self.root)
        ReportWindow(new_window, self.library)

    def open_borrow_return_window(self):
        new_window = ctk.CTkToplevel(self.root)
        BorrowReturnWindow(new_window, self.library)

    def show_load_message(self):
        messagebox.showinfo("Welcome", "Data loaded from the last session successfully.")

    def save_data(self):
        self.library.save_data()
        messagebox.showinfo("Success", "Data saved successfully!")