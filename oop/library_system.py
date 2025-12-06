class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size  # in MB

    def __str__(self):
        return f'EBook: {self.title} by {self.author}, Size: {self.file_size}KB'

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.file_size})"
    

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count  # in grams

    def __str__(self):
        return f'Printed Book: {self.title} by {self.author}, page_count: {self.page_count}KB'

    def __repr__(self):
        return f"PrintedBook('{self.title}', '{self.author}', {self.page_count})"
    

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f'Added: {book}')

    def list_books(self):
        for book in self.books:
            print(book)