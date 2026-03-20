from user import User

class Member(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name)
        self.borrowed_books = 0

    def borrow_book(self, book):
        if self.borrowed_books >= 5:
            print("Borrow limit reached (max 5 books).")
            return

        if book.status == "Available":
            book.borrow_book()
            self.borrowed_books += 1
        else:
            print(f"{book.title} is already borrowed.")

    def return_book(self, book):
        if book.status == "Borrowed":
            book.return_book()
            self.borrowed_books -= 1
        else:
            print(f"{book.title} was not borrowed.")