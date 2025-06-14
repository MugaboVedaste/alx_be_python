class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True

    def return_book(self):
        """Mark the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False

    def is_available(self):
        """Check if the book is currently available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []  # private list to store books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by its title if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                return
        print(f"Book '{title}' is not available.")

    def return_book(self, title):
        """Return a book to the library by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        """Print all available books."""
        available = [book for book in self._books if book.is_available()]
        for book in available:
            print(f"{book.title} by {book.author}")
        if not available:
            print("No books are currently available.")
