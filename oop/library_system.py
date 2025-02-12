class Book:
    """Base class representing a book."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    """Represents an electronic book (EBook), inheriting from Book."""
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size
    
    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
    """Represents a printed book (PrintBook), inheriting from Book."""
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
    
    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    """Represents a library that stores books using composition."""
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """Adds a book (Book, EBook, or PrintBook) to the library."""
        self.books.append(book)
    
    def list_books(self):
        """Prints details of each book in the library."""
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)

