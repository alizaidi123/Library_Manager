import os

LIBRARY_FILE = "library.txt"

def load_lib():
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE,"r") as file:
            library = eval(file.read())
        return library
    return []

def save_lib(library):
    with open(LIBRARY_FILE,"w") as file:
        file.write(str(library))

def add_book(library):
    title = input("Enter the book's title")
    author = input("Enter the name of the author")
    year = input("Enter the publication year")
    genre = input("Enter the genre")
    read_status = input("Have you read this book before? (yes/no):").lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    library.append(book)
    print("Book is successfully added!")

def remove_book(library):
    title = input("Enter the book's title")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("Book is successfully removed!")
            return
    print("Book not found")

def search_book(library):
    print("Search by:")
    print("1: by Title")
    print("2: by Author")
    choice = input("Enter your choice: 1 or 2")

    if choice == "1":
        title = input("Enter the book's title")
        match_book = [book for book in library if title.lower() in book["title"].lower()]

    elif choice == "2":
        author = input("Enter the name of the author")
        match_book = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("No such book was found")
        return
    if match_book:
        print("Matching Book")
        for i, book in enumerate(library,1):
            status = "Read" if book["read_status"] else "Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching book was found")

def display_all_books(library):
    if not library:
        print("Your library is empty")
        return
    print("Your Library:")
    for i, book in enumerate(library,1):
        status = "Read" if book["read_status"] else "Unread"
        print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")

def display_stats(library):
     total_books = len(library)
     read_books = sum(book["read_status"]for book in library)
     read_percentage = (read_books/total_books)*100 if total_books > 0 else 0

     print(f"Total books in Library: {total_books}")
     print(f"Total books you have read from the Library {read_books}")
     print(f"Percentage of books you have read {read_percentage}")

def main():
    library = load_lib()

    while True:
        print("\nMenu")
        print("Welcome to your Personal Library Manager!")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: 1 to 6 ")

        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_stats(library)
        elif choice == "6":
            save_lib(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()