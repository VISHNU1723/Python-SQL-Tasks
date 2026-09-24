# Library Management System
# Uses functions and file handling

FILE_NAME = "library.txt"


def add_book():
    book_id = input("Enter Book ID: ")
    book_name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{book_id},{book_name},{author}\n")

    print("Book added successfully.")


def view_books():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

            if not books:
                print("No books available.")
                return

            print("\n===== Library Books =====")

            for book in books:
                data = book.strip().split(",")

                if len(data) == 3:
                    print(
                        f"Book ID: {data[0]} | "
                        f"Book Name: {data[1]} | "
                        f"Author: {data[2]}"
                    )

    except FileNotFoundError:
        print("No library file found. Add a book first.")


def search_book():
    search_id = input("Enter Book ID to search: ")

    try:
        with open(FILE_NAME, "r") as file:
            for book in file:
                data = book.strip().split(",")

                if len(data) == 3 and data[0] == search_id:
                    print("\nBook Found")
                    print(f"Book ID: {data[0]}")
                    print(f"Book Name: {data[1]}")
                    print(f"Author: {data[2]}")
                    return

        print("Book not found.")

    except FileNotFoundError:
        print("No library file found.")


def delete_book():
    delete_id = input("Enter Book ID to delete: ")

    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()

        found = False

        with open(FILE_NAME, "w") as file:
            for book in books:
                data = book.strip().split(",")

                if len(data) == 3 and data[0] == delete_id:
                    found = True
                else:
                    file.write(book)

        if found:
            print("Book deleted successfully.")
        else:
            print("Book not found.")

    except FileNotFoundError:
        print("No library file found.")


def main():
    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()

        elif choice == "2":
            view_books()

        elif choice == "3":
            search_book()

        elif choice == "4":
            delete_book()

        elif choice == "5":
            print("Thank you for using Library Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
