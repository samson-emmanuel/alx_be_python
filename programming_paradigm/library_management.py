class Book:
    def __init__(self, title, author):
        self.title = title                # public
        self.author = author              # public
        self._is_checked_out = False      # private

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False


class Library:
    def __init__(self):
        self._books = []      # private list of Book objects

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Try to check out a book by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # book not found

    def return_book(self, title):
        """Try to return a book by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # book not found

    def list_available_books(self):
        """Return a list of (title, author) for books not checked out."""
        return [
            (book.title, book.author)
            for book in self._books
            if not book._is_checked_out
        ]
