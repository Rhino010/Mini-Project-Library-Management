class Book:

    def __init__(self, title, author, genre, publication_year):
        self.title = title
        self.author = author
        self.genre = genre
        self.publication_year = publication_year
        self.availability = True
        self.books = {}

    def add_book(self, title, author, genre, publication_year, availability):
        self.books[self.title] = {}
        self.books[self.title]['author'] = self.author
        self.books[self.title]['genre'] = self.genre
        self.books[self.title]['year'] = self.publication_year
        self.books[self.title]['available'] = self.availability
        print(self.books)

    def borrow_book(self):
        if self.books[self.title]['availability'] == True:
            self.books[self.title]['availability'] = False
        else:
            print("That book is not available at this time.")

    def return_book(self):
        try:
            if self.books[self.title]['available']== False:
                self.books[self.title]['available'] = True
        except Exception as e:
            print(f"An error has occurred: {e}")

    def find_book(self):
        if self.title in self.books and self.books[self.title]['available'] == True:
            print(f"{self.title} has been found and is available to check out.")
        elif self.title in self.books and self.books[self.title]['available'] == False:
            print(f"{self.title} is provided by this library but is already checked out. Please try again later.")
        else:
            print("Sorry but we do not currently carry that book.")


    def show_all_books(self):
        for book in self.books:
            print(f"{book}, Author: {book['author']}, Genre: {book['genre']}, Publication Year: {book['year']}, Availability: {book['availability']}")
        
