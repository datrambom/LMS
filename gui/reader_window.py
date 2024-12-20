import customtkinter as ctk
from tkinter import messagebox
from models.reader import Reader


class ReaderWindow:
    def __init__(self, root, library):
        self.root = root
        self.library = library
        self.root.title("Manage Readers")

        # Поля ввода
        self.first_name_entry = ctk.CTkEntry(root, width=100)
        self.last_name_entry = ctk.CTkEntry(root, width=100)
        self.ticket_number_entry = ctk.CTkEntry(root, width=100)

        # Метки
        ctk.CTkLabel(root, text="First Name:").grid(row=0, column=0)
        ctk.CTkLabel(root, text="Last Name:").grid(row=1, column=0)
        ctk.CTkLabel(root, text="Ticket Number:").grid(row=2, column=0)

        # Расположение полей
        self.first_name_entry.grid(row=0, pady=5, column=1)
        self.last_name_entry.grid(row=1, pady=5, column=1)
        self.ticket_number_entry.grid(row=2, pady=5, column=1)

        # Кнопки
        ctk.CTkButton(root, text="Add Reader", command=self.add_reader).grid(row=3, column=0, pady=5, padx=5)
        ctk.CTkButton(root, text="Delete Reader", command=self.delete_reader).grid(row=3, column=1, pady=5, padx=5)
        ctk.CTkButton(root, text="View Readers",
                      command=self.view_readers).grid(row=4, column=0, pady=5, padx=5, columnspan=2)

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
        """Удаляет читателя по номеру читательского билета."""
        ticket_number = self.ticket_number_entry.get().strip()

        if not ticket_number:
            messagebox.showerror("Error", "Please enter a ticket number.")
            return

        # Найти читателя
        readers = [reader for reader in self.library.readers if reader.ticket_number == ticket_number]

        if not readers:
            messagebox.showerror("Error", "Reader with this ticket number not found.")
            return

        # Удалить читателя
        reader_to_remove = readers[0]  # В списке будет только один элемент
        self.library.readers.remove(reader_to_remove)
        self.library.save_data()
        messagebox.showinfo("Success",
                            f"Reader {reader_to_remove.first_name} {reader_to_remove.last_name} has been removed.")
        self.ticket_number_entry.delete(0, ctk.END)

    def view_readers(self):
        readers = self.library.readers
        if readers:
            reader_list = "\n".join(str(reader) for reader in readers)
            messagebox.showinfo("Readers", reader_list)
        else:
            messagebox.showinfo("Readers", "No readers available.")
