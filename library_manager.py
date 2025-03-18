import os

# File to store library data
LIBRARY_FILE = "library.txt"

# Function to load the library from a file
def load_library():
    library = []
    if os.path.exists(LIBRARY_FILE):
        with open(LIBRARY_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    try:
                        title, author, year, genre, read_status = line.split("|")
                        book = {
                            "title": title,
                            "author": author,
                            "year": int(year),
                            "genre": genre,
                            "read_status": read_status == "True"
                        }
                        library.append(book)
                    except ValueError:
                        print(f"⚠️ Skipping invalid line in library.txt: {line}")
    return library

# Function to save the library to a file
def save_library(library):
    with open(LIBRARY_FILE, "w") as file:
        for book in library:
            file.write(f"{book['title']}|{book['author']}|{book['year']}|{book['genre']}|{book['read_status']}\n")

# Function to display the menu
def display_menu():
    print("\n📚 Welcome to your Personal Library Manager! 📚")
    print("1. Add a book 📖")
    print("2. Remove a book 🗑️")
    print("3. Search for a book 🔍")
    print("4. Display all books 📜")
    print("5. Display statistics 📊")
    print("6. Exit 🚪")
    print("Enter your choice: ", end="")

# Function to add a book
def add_book(library):
    print("\n➕ Add a Book ➕")
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_status = input("Have you read this book? (yes/no): ").lower() == "yes"
    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    library.append(book)
    print("✅ Book added successfully!")

# Function to remove a book
def remove_book(library):
    print("\n🗑️ Remove a Book 🗑️")
    title = input("Enter the title of the book to remove: ")
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            print("✅ Book removed successfully!")
            return
    print("❌ Book not found!")

# Function to search for a book
def search_book(library):
    print("\n🔍 Search for a Book 🔍")
    print("Search by:")
    print("1. Title 📖")
    print("2. Author ✍️")
    choice = input("Enter your choice: ")
    if choice == "1":
        title = input("Enter the title: ")
        matching_books = [book for book in library if title.lower() in book["title"].lower()]
    elif choice == "2":
        author = input("Enter the author: ")
        matching_books = [book for book in library if author.lower() in book["author"].lower()]
    else:
        print("❌ Invalid choice!")
        return

    if matching_books:
        print("\n📚 Matching Books 📚")
        for i, book in enumerate(matching_books, 1):
            status = "✅ Read" if book["read_status"] else "❌ Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("❌ No matching books found!")

# Function to display all books
def display_all_books(library):
    if library:
        print("\n📚 Your Library 📚")
        for i, book in enumerate(library, 1):
            status = "✅ Read" if book["read_status"] else "❌ Unread"
            print(f"{i}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("❌ Your library is empty!")

# Function to display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = sum(book["read_status"] for book in library)
    percentage_read = (read_books / total_books * 100) if total_books > 0 else 0
    print("\n📊 Library Statistics 📊")
    print(f"📚 Total books: {total_books}")
    print(f"✅ Percentage read: {percentage_read:.1f}%")

# Main function
def main():
    library = load_library()
    while True:
        display_menu()
        choice = input()
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_all_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("\n📁 Library saved to file. Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice! Please try again.")

if __name__ == "__main__":
    main()