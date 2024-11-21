from book import Book, BookManager
from user import User
from author import Author

import os

def main():
    
    while True:
      
        print("Main Menu\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        choice = input("Please make your selection:\n")

        if choice == '1':
            print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
            selection = input("\nPlease make your selection:\n")
            if selection == '1':
                title = input("Enter the title:\n")
                author = input("Enter the author:\n")
                genre = input("Enter the genre:\n")
                year = input("Enter the publication year:\n")
                availability = True
                book_ops.add_book(title, author, genre, year, availability)

            elif selection == '2':
                pass
            elif selection == '3':
                pass
            elif selection == '4':
                pass
            elif selection == '5':
                pass

        elif choice == '2':
            print("\nUser Operations:\n1. Add a new user\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
            selection = input("\nPlease make your selection:\n")
            if selection =='1':
                pass
            elif selection == '2':
                pass
            elif selection == '3':
                pass
            elif selection =='4':
                pass
            elif selection == '5':
                pass

        elif choice == '3':
            print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
            selection = input("\nPlease make your selection:\n")
            if selection == '1':
                pass
            elif selection == '2':
                pass
            elif selection == '3':
                pass

        elif choice == '4':
            print("Closing program....")
            break


if __name__ == "__main__":
    main()