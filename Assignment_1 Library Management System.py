class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"{self.title} by {self.author} - {status}"


class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.is_borrowed = True
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' is already borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.is_borrowed = False
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print(f"Book '{title}' added.")

    def register_patron(self, name):
        self.patrons.append(Patron(name))
        print(f"Patron '{name}' registered.")

    def show_books(self):
        if not self.books:
            print("No books yet.")
        else:
            for book in self.books:
                print(book)

    def show_patrons(self):
        if not self.patrons:
            print("No patrons yet.")
        else:
            for patron in self.patrons:
                print(f"{patron.name} - Borrowed: {[b.title for b in patron.borrowed_books]}")

    # ✅ Borrow and Return handled here
    def borrow_book(self, pname, btitle):
        patron = None
        book = None
        for p in self.patrons:
            if p.name == pname:
                patron = p
        for b in self.books:
            if b.title == btitle:
                book = b
        if patron and book:
            patron.borrow_book(book)
        else:
            print("Patron or Book not found.")

    def return_book(self, pname, btitle):
        patron = None
        book = None
        for p in self.patrons:
            if p.name == pname:
                patron = p
        for b in self.books:
            if b.title == btitle:
                book = b
        if patron and book:
            patron.return_book(book)
        else:
            print("Patron or Book not found.")


def menu():
    lib = Library()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. Register Patron")
        print("3. Show Books")
        print("4. Show Patrons")
        print("5. Borrow Book")
        print("6. Return Book")
        print("0. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            t = input("Book title: ")
            a = input("Author: ")
            lib.add_book(t, a)
        elif choice == '2':
            n = input("Patron name: ")
            lib.register_patron(n)
        elif choice == '3':
            lib.show_books()
        elif choice == '4':
            lib.show_patrons()
        elif choice == '5':
            pname = input("Patron name: ")
            btitle = input("Book title: ")
            lib.borrow_book(pname, btitle)
        elif choice == '6':
            pname = input("Patron name: ")
            btitle = input("Book title: ")
            lib.return_book(pname, btitle)
        elif choice == '0':
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")
            

# Run the program
menu()
