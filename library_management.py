class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"'{self.title}' borrowed.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"'{self.title}' returned.")
        else:
            print(f"'{self.title}' was not borrowed.")


class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book and book.is_available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f"Sorry {self.name}, '{book.title if book else 'Unknown'}' is not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f"{self.name} doesn't have '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def add_member(self, member):
        self.members.append(member)
        print(f"Added member '{member.name}'.")

    def find_book(self, title):
        return next((b for b in self.books if b.title.lower() == title.lower()), None)


if __name__ == "__main__":
    library = Library()

    b1 = Book("The Giant Man", "Xmas", "12345")
    b2 = Book("Lion King", "Mighty Raju", "67890")
    library.add_book(b1)
    library.add_book(b2)

    m1 = Member("Satish", "M001")
    m2 = Member("Vinod", "M002")
    library.add_member(m1)
    library.add_member(m2)

    book = library.find_book("Lion King")
    m1.borrow_book(book)
    m1.borrow_book(book)
    m2.return_book(book)
    m2.borrow_book(book)
