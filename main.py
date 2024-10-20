class Book:
    def __init__(self, book_id, name, author, genre, publication_year, isbn):
        self.book_id = book_id
        self.name = name
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.isbn = isbn
        self.quantity = 0

    def update_quantity(self, quantity):
        self.quantity = quantity

    def get_details(self):
        return {"Book id": self.book_id,
                "Name": self.name,
                "Author": self.author,
                "Genre": self.genre,
                "Publication Year": self.publication_year,
                "ISBN": self.isbn,
                "Quantity": self.quantity}

    def check_out(self):
        if self.quantity > 0:
            self.quantity -= 1
            return True
        else:
            return False

    def return_book(self):
        self.quantity += 1

class LibraryInventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        book_to_remove = self.get_book(book_id)
        if book_to_remove:
            self.books.remove(book_to_remove)

    def get_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                return book
        return None

    def list_books(self):
        return [book.get_details() for book in self.books]

    def update_inventory(self, book_id, quantity):
        book = self.get_book(book_id)
        if book:
            return book.quantity
        return 0
class Report:
    def __init__(self, inventory):
        self.inventory = inventory

    def low_stock_report(self, threshold):
        return [book.get_details() for book in self.inventory.books if book.quantity < threshold]

    def genre_report(self, genre):
        return [book.get_details() for book in self.inventory.books if book.genre == genre]

    def author_report(self, author):
        return [book.get_details() for book in self.inventory.books if book.author == author]

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def login(self):
        pass

    def get_permission(self):
        pass

    def perform_inventory_actions(self, inventory, action, book=None, quantity=None):
        if self.role == 'admin':
            if action == 'add':
                inventory.add_book(book)
            elif action == 'remove':
                inventory.remove_book(book.book_id)
            elif action == 'update':
                inventory.update_inventory(book.book_id, quantity)
        elif self.role == 'librarian':
            if action == 'check_out':
                if book.check_out():
                    print(f"Checked out: {book.name}")
                else:
                    print(f"Out of stock: {book.name}")
            elif action == 'return':
                book.return_book()
        else:
            print("Permission denied")
def main():
    inventory = LibraryInventory()

    book1 = Book(12150, "Harry Potter and the Philosopher's Stone", "J.K. Rowling", "Fantasy", 1997, "978-0-7475-3269-9")
    book1.update_quantity(50)
    inventory.add_book(book1)

    book2 = Book(12138, "To Kill a Mockingbird", "Harper Lee", "Southern Gothic", 1960, "978-0-0609-3546-7")
    book2.update_quantity(3)
    inventory.add_book(book2)

    for book in inventory.list_books():
        print(book)

    report = Report(inventory)
    low_stock_books = report.low_stock_report(4)
    print("Low stock books:", low_stock_books)

    admin = User("Admin150","admin")
    ibrarian = User("Librarian120", "librarian")

    new_book = Book(1,"The King’s Avatar", "Hudie Lan", "Competitive Gaming", 2011, "978-7-5353-6287-2")
    new_book.update_quantity(100)
    admin.perform_inventory_actions(inventory, 'add', book=new_book)
    admin.perform_inventory_actions(inventory,'remove', book=book2)
    admin.perform_inventory_actions(inventory, 'check_out', book=book1)

    for book in inventory.list_books():
        print(book)

if __name__ == '__main__':
    main()