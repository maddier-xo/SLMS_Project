from book import Book
from member import Member

def main():
    # fashion-themed books
    book1 = Book(1, "The Art of Fashion", "Anna Thompson")
    book2 = Book(2, "Street Style Trends", "James Carter")
    book3 = Book(3, "History of Couture", "Sophie Bennett")
    book4 = Book(4, "Sustainable Fashion Guide", "Rachel Adams")
    book5 = Book(5, "Wardrobe Essentials", "Liam Roberts")
    book6 = Book(6, "Fashion Photography", "Emily White")  

    books = [book1, book2, book3, book4, book5, book6]

    # Create a member
    member1 = Member(101, "Hi Penny")
    member1.login()

    while True:
        print("\nLibrary Menu")
        print("1. Borrow Book")
        print("2. Return Book")
        print("3. View All Books")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            # Show available books
            print("\nBooks Available:")
            for i, book in enumerate(books):
                print(f"{i+1}. {book.title} ({book.status})")
            selection = int(input("Enter the number of the book to borrow: ")) - 1
            if 0 <= selection < len(books):
                member1.borrow_book(books[selection])
            else:
                print("Invalid selection.")

        elif choice == "2":
            # Show borrowed books
            borrowed_books = [book for book in books if book.status == "Borrowed"]
            if not borrowed_books:
                print("\nNo books borrowed.")
                continue
            print("\nBooks Borrowed:")
            for i, book in enumerate(borrowed_books):
                print(f"{i+1}. {book.title}")
            selection = int(input("Enter the number of the book to return: ")) - 1
            if 0 <= selection < len(borrowed_books):
                member1.return_book(borrowed_books[selection])
            else:
                print("Invalid selection.")

        elif choice == "3":
            print("\nAll Books Info:")
            for book in books:
                book.display_book()

        elif choice == "4":
            print("Exiting system.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
