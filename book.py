class LibraryBook:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "Available"  # Available, Borrowed, Reserved

    def borrow_book(self):
        if self.status == "Available":
            self.status = "Borrowed"
            print(f"{self.title} you have borrowed.")
        else:
            print(f"{self.title} is currently not available.")

    def return_book(self):
        if self.status == "Borrowed":
            self.status = "Available"
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} was not borrowed.")

    def display_book(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")