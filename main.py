import customtkinter as ctk
from models.library import Library
from gui.main_window import MainWindow

if __name__ == "__main__":
    library = Library()
    root = ctk.CTk()
    app = MainWindow(root, library)

    root.mainloop()
