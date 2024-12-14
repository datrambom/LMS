import tkinter as tk
from models.library import Library
from gui.main_window import MainWindow

if __name__ == "__main__":
    library = Library()
    root = tk.Tk()
    app = MainWindow(root, library)
    root.mainloop()
