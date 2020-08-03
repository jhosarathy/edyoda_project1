# -*- coding: utf-8 -*-
from Book import Book
from Singleton import Singleton
# First Book is file & second is Class


class Catalog(Singleton):
    '''
    A subclass of Singleton class to represent Books in Library
    ...

    Attribute
    ---------
    diifferent_book_count : int
        Initially 0 and increments as books are added to the Library
    books : Object of class list
        List of different Objects of Book class

    Methods
    -------

    __init__():
        Constructs all the necessary attributes for the Book object
    addBook(name,author,publish_date,pages):
        Creates a Book object and appends it to the books list
    addBookItem(book, isbn,rack):
        Adds a new copy of the already existing book to the book_item
    searchByName(name):
        Returns the Book object whose name attribute is same as the argument passed.
    searchByNameIndex(name):
        Returns the Book object whose name attribute is same as the argument passed.
        Returns the Book object's index in the books list.
    searchByAuthor(author):
        Returns the Book object whose author attribute is same as the argument passed.
    displayAllBooks():
        Prints the total count of different books available in Library for issue.
        Prints all the available books.
        Prints the total count of all the books including the copies available in Library for issue.
    removeBook(name):
        Removes a book from the books list.
    removeBookItem(name, isbn):
        Removes a book copy from book_item.

    '''
    def __init__(self):
        '''
        Constructs all the necessary attributes for the Book object
        ...
        Parameters:
        ----------
        diifferent_book_count : int
            Initially 0 and increments as books are added to the Library
        books : Object of class list
            List of different Objects of Book class

        '''
        self.different_book_count = 0
        self.books = []

    # Only available to admin
    def addBook(self, name, author, publish_date, pages):
        '''
        Creates a Book object and appends it to the books list
        ...
        Parameters
        ----------
        name : str
            Name of the book 
        author : str
            Author of the book 
        publish_date : str
            The year in which the book got published
        pages : int
            Number of pages in that book

        Returns
        -------
        Book object

        '''
        for existing_book in self.books:
            if existing_book.name == name:
                return None
        b = Book(name, author, publish_date, pages)
        if b not in self.books:
            self.different_book_count += 1
            self.books.append(b)
        return b
    
    # Only available to admin
    def addBookItem(self, book_name, isbn, rack):
        '''
        Adds a new copy of the already existing book to the book_item
        ...
        Parameters
        ----------
        book: str
            Name of the book to which we've to add the ISBN
        isbn : string
            The unique identity number for each copy of the book
        rack: string
            Shelf where the book is placed in the physical library

        Returns
        -------
        Status of the method. (If added or not with reason)

        '''
        for i, cur_book in enumerate(self.books):
            if cur_book.name == book_name:
                cur_book.addBookItem(isbn, rack)
                return f"ADD_BOOK_ITEM_SUCCESS: {book_name}: Added book_item with ISBN {isbn}"
        return f"ADD_BOOK_ITEM_FAILURE: {book_name} not found"

    def searchByName(self, name):
        '''
        Returns the Book object whose name attribute is same as the argument passed.
        ...

        Parameters
        ----------
        name : str
            Name of the Book

        Returns
        -------
        Book object if book is present else None

        '''
        for book in self.books:
            if name == book.name:
                return book
        return None
    
    def searchByNameIndex(self, name):
        '''
        Returns the Book object whose name attribute is same as the argument passed.

        Returns the Book object's index in the books list. 
        ...
        Parameters
        ----------
        name : str
            Name of the Book

        Returns
        -------
        Book object and it's index in book list if book is present, else None

        '''
        for i, book in enumerate(self.books):
            if name.strip() == book.name:
                return [i, book]
        return [-1, None]
    
    def searchByAuthor(self, author):
        '''
        Returns the Book object whose author attribute is same as the argument passed.
        ...
        Parameters
        ----------
        name : str
            Name of the Book

        Returns
        -------
        Book object if book is present else None

        '''
        for book in self.books:
            if author.strip() == book.author:
                return book
        
    def displayAllBooks(self):
        '''
        Prints the total count of different books available in Library for issue.
        Prints all the available books.
        Prints the total count of all the books including the copies available in Library for issue.
        ...

        '''
        print("---------------LIBRARY_CATALOG---------------")
        print(f"DIFFERENT_BOOK_COUNT: {self.different_book_count}")
        c = 0
        for book in self.books:
            c += book.total_count
            print(book)
            book.printBook()
        print(f"TOTAL_BOOK_COPIES: {c}")
        print("---------------LIBRARY_CATALOG---------------")

    def removeBook(self, name):
        '''
        Removes a book from the books list.
        ...
        Parameters
        ----------
        name : str
            Name of the Book    

        '''

        [bookIndex, book] = self.searchByNameIndex(name)
        if bookIndex != -1:
            del self.books[bookIndex]
            self.different_book_count -= 1
            return f"REMOVE_SUCCESS: {book.name} got removed"
        else:
            return f"REMOVE_FAILURE: Book {name} not found"

    def removeBookItem(self, name, isbn):
        '''
        Searches a book object and removes it's copy from book_item.
        ...

        Parameters
        ----------
        name : str
            Name of the Book
        isbn : string
            The unique identity number for each copy of the book

        '''
        book = self.searchByName(name)
        if book is not None:
            book_item = book.searchBookItem(isbn)
            book.removeBookItem(book_item)
            return name + " with isbn : " + book_item.isbn + " got removed."
        return name + "doesn't exist in the library"
        

