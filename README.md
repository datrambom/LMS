# Library Management System (LMS)

Welcome to the **Library Management System (LMS)**! This is a Python-based application designed to automate book and reader management in libraries. Featuring a sleek graphical user interface (GUI) built with `customtkinter`.

## Key Features

### 📚 **Books Management**
- Add new books to the library.
- Update existing book details (e.g., title, author, genre).
- Delete books no longer available.
- Track borrowed books.

### 👥 **Readers Management**
- Register new readers with a unique library card number.
- Update reader details (e.g., name, contact info).
- Delete inactive readers.
- Track borrowed books by each reader.

### 📊 **Reports and Analytics**
- Generate reports on:
  - Borrowed books currently in store.
  - Total number of books by genre.
  - Overall book inventory.
  - Readers' borrowing history.

### 💾 **Data Persistence**
- Save all data (books, readers, borrowed books) to JSON files.
- Automatically load data from the last session on startup.
- Preserve borrowing history and inventory changes across sessions.

## Known Issues
- The current version does not support real-time multi-user access.
- Advanced search features (e.g., fuzzy search) are yet to be implemented.
