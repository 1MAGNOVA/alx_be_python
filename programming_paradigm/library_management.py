class Book:
    """Represents a book with a title, author, and checkout status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Marks the book as checked out if available."""
        if self._is_checked_out:
            return False
        self._is_checked_out = True
        return True

    def return_book(self):
        """Marks the book as available again."""
        self._is_checked_out = False

    def is_available(self):
        """Returns True if the book is available, False otherwise."""
        return not self._is_checked_out

class Library:
    """Represents a library that manages a collection of books."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Marks a book as checked out if it is available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"'{title}' has been checked out.")
                return
        print(f"Sorry, '{title}' is not available.")

    def return_book(self, title):
        """Marks a book as returned if it exists in the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out.")

    def list_available_books(self):
        """Prints a list of available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
