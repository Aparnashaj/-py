class Book:
    def __init__(self, name, author):
        self.name = name
        self.author = author
        self.available = True

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        return found_books

if __name__ == "__main__":
    library = Library()
    book1 = Book("Python Basics", "aparna")
    book2 = Book("Data Structures", "adarsh")
    book3 = Book("Algorithms", "monika")
    book4 = Book("oops concepts","aparna")
    book5 = Book("functiinal programming","aadhi")

    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5)
    author_to_search = input("Enter the author's name: ")
    found_books = library.find_book_by_author(author_to_search)

    if found_books:
        print(f"Books by {author_to_search}:")
        for book in found_books:
            print(f"- {book.name}")
    else:
        print(f"No books found by {author_to_search}.")