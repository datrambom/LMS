import customtkinter as tk
from tkinter import messagebox

class BorrowReturnWindow:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Borrow/Return Books")

        # Widgets for Reader Ticket Number
        tk.CTkLabel(root, text="Reader Ticket Number:").grid(row=0, column=0)
        self.ticket_entry = tk.CTkEntry(root, width=100)
        self.ticket_entry.grid(row=0, pady=5, column=1)

        # Widgets for Book Title
        tk.CTkLabel(root, text="Book Title:").grid(row=1, column=0)
        self.book_entry = tk.CTkEntry(root, width=100)
        self.book_entry.grid(row=1, pady=5, column=1)

        # Buttons for Borrow and Return
        tk.CTkButton(root, text="Borrow Book", command=self.borrow_book).grid(row=2, column=0, pady=5, padx=5)
        tk.CTkButton(root, text="Return Book", command=self.return_book).grid(row=2, column=1, pady=5, padx=5)

    def borrow_book(self):
        ticket_number = self.ticket_entry.get()
        book_title = self.book_entry.get()
        if not (ticket_number and book_title):
            messagebox.showerror("Error", "Both fields are required.")
            return

        result = self.library.borrow_book(ticket_number, book_title)
        messagebox.showinfo("Borrow Book", result)

    def return_book(self):
        ticket_number = self.ticket_entry.get()
        book_title = self.book_entry.get()
        if not (ticket_number and book_title):
            messagebox.showerror("Error", "Both fields are required.")
            return

        result = self.library.return_book(ticket_number, book_title)
        messagebox.showinfo("Return Book", result)
