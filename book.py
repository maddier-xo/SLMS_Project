class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.status = "Available"  # Available books 

    def borrow_book(self):
        # Check if the book is currently available
        if self.status == "Available":
            # If available, change the status to borrowed
            self.status = "Borrowed"
            print(f"{self.title} you have borrowed.")
        else:
             # If not available, tell the user that the book is already borrowed
            print(f"{self.title} is currently not available.")

    def return_book(self):
          # Check if the book is currently borrowed
        if self.status == "Borrowed":
             # If borrowed, change the status back to available
            self.status = "Available"
            print(f"{self.title} has been returned.")
        else:
             # If the book was not borrowed tell the user
            print(f"{self.title} was not borrowed.")

    def display_book(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Status: {self.status}")
