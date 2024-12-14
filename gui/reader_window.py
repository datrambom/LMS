import tkinter as tk
from tkinter import messagebox
from models.reader import Reader

class ReaderWindow:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Manage Readers")

        # Поля ввода
        self.first_name_entry = tk.Entry(root, width=30)
        self.last_name_entry = tk.Entry(root, width=30)
        self.ticket_number_entry = tk.Entry(root, width=30)

        # Метки
        tk.Label(root, text="First Name:").grid(row=0, column=0)
        tk.Label(root, text="Last Name:").grid(row=1, column=0)
        tk.Label(root, text="Ticket Number:").grid(row=2, column=0)

        # Расположение полей
        self.first_name_entry.grid(row=0, column=1)
        self.last_name_entry.grid(row=1, column=1)
        self.ticket_number_entry.grid(row=2, column=1)

        # Кнопки
        tk.Button(root, text="Add Reader", command=self.add_reader).grid(row=3, column=0, pady=10)
        tk.Button(root, text="Delete Reader", command=self.delete_reader).grid(row=3, column=1, pady=10)
        tk.Button(root, text="View Readers", command=self.view_readers).grid(row=4, column=0, pady=10, columnspan=2)

    def add_reader(self):
        first_name = self.first_name_entry.get()
        last_name = self.last_name_entry.get()
        ticket_number = self.ticket_number_entry.get()

        if not (first_name and last_name and ticket_number):
            messagebox.showerror("Error", "All fields are required.")
            return

        reader = Reader(first_name, last_name, ticket_number)
        self.library.add_reader(reader)
        messagebox.showinfo("Success", "Reader added successfully.")

    def delete_reader(self):
        ticket_number = self.ticket_number_entry.get()
        readers = self.library.find_reader(ticket_number=ticket_number)
        if readers:
            self.library.readers.remove(readers[0])
            messagebox.showinfo("Success", "Reader deleted successfully.")
        else:
            messagebox.showerror("Error", "Reader not found.")

    def view_readers(self):
        readers = self.library.readers
        if readers:
            reader_list = "\n".join(str(reader) for reader in readers)
            messagebox.showinfo("Readers", reader_list)
        else:
            messagebox.showinfo("Readers", "No readers available.")