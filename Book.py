# -*- coding: utf-8 -*-
from BookItem import BookItem
import time
import datetime


class Book:
    '''
    A class to represent a Book
    ...

    Attribute
    ---------

    name: str
        Name of the book 
    author: str
        Author of the book 
    publish_date : str
         The year in which the book got published
    pages : int
        Number of pages in that book
    total_count : int
        Total number of books present in the library
    book_item : list
        list of objects of BookItem class

    Methods
    -------

    __init__(name, author, publish_date, pages):
        Constructs all the necessary attributes for the Book object
    __repr__():
        Represents the Book and its author, recently added by the catalog class to the library.
    addBookItem(isbn,rack):
        Adds a new copy of the already existing book to the book_item
    printBook():
        Prints Book's name and author. Also, prints the isbn if a copy of that book exists already.
    searchBookItem(isbn):
        Searches book_item list and returns a BookItem object 
    removeBookItem(book_item)
        Searches a book object and removes it's copy from book_item
    '''

    def __init__(self, name, author, publish_date, pages):
        '''
        Constructs all the necessary attributes for the person object.
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
        total_count : int
            Total number of books present in the library
        book_item : list
            list of objects of BookItem class

        '''
        self.name = name
        self.author = author
        self.publish_date = publish_date
        self.pages = pages
        self.total_count = 0
        self.borrowed = 0
        self.book_item = []

    def __repr__(self):
        '''
        Represents the Book and its author, recently added by the catalog class to the library.
        ...

        Returns
        -------
        Formatted string : This mentions the name, author and number of copies of the book in the library.

        '''
        return f"[Book: {self.name}, Author: {self.author}, NumCopies: {len(self.book_item)}]"

    def addBookItem(self, isbn, rack):
        '''
        Adds a new copy of the already existing book to the catalog
        ...

        Parameters
        ----------
        isbn : string
            The unique identity number for each copy of the book
        rack: string
            Shelf where the book is placed in the physical library

        Returns
        -------
        True : The book gets added to the library

        '''

        b = BookItem(self, isbn, rack)
        self.book_item.append(b)
        self.total_count += 1
        return True

    def updateBorrowedCount(self, inc):
        self.borrowed += inc

    def printBook(self):
        '''
        Prints Book's name and author. Also, prints the isbn if a copy of that book exists already.

        Returns
        -------
        True : The book's isbn, name and author are printed
        '''

        for bi in self.book_item:
            print(f"(ISBN: {bi.isbn}, RACK: {bi.rack})")
        return True

    def searchBookItem(self, isbn):
        '''
        searches book_item list and returns a BookItem object
        ...

        Parameters
        ----------
        isbn : str
            The unique identity number for each copy of the book

        Returns
        -------
        True: The bookItem object based on isbn is searched and returned

        '''
        for book_item in self.book_item:
            if isbn.strip() == book_item.isbn:
                return book_item
        return True

    def removeBookItem(self, book_item):
        '''
        Searches a book object and removes it's copy from book_item
        ...

        Parameters
        ----------
        book_item : object of class BookItem 
            It has unique isbn and rack as its attributes

        Returns
        -------
        book_item: This object gets removed from book_items list of book

        '''
        for item in self.book_item:
            if book_item.isbn == item.isbn:
                self.book_item.remove(book_item)
                self.total_count -= 1
                return book_item
        return None


class BookIssue:
    '''
    A class to keep track of all the books issued to a member of library
    ...

    Attributes
    ----------
    is_issued: bool
        Status of the book to be issued from Library to Member
    message: str
        The message regarding the book issue to the member
    isbn: str 
        The unique identity number for each copy of the book
    rack: str 
        Shelf where the book is placed in the physical library
    days: int
        Number of days a member can have the book issued without penalty

    Methods
    -------
    __init__(is_issued, message, isbn, rack, days):
        Constructs all the necessary attributes for the Book object
    __repr__():
        Represents the Issued status of the book asked for by the member of Library.
        Represents the Book_items details that is to be issued from the Library.

    '''

    def __init__(self, is_issued, message, isbn, rack, days):
        '''
        Constructs all the necessary attributes for the Book object
        ...

        Parameters:
        ----------
        is_issued: bool
            Status of the book to be issued from Library to Member
        message: str
            The message regarding the book issue to the member
        isbn: str 
            The unique identity number for each copy of the book
        rack: str 
            Shelf where the book is placed in the physical library
        days: int
            Number of days a member can have the book issued without penalty
        borrowed: int
            Epoch of the moment when the book was issued to the member

        '''
        self.is_issued = is_issued
        self.message = message
        self.isbn = isbn
        self.rack = rack
        self.days = days
        self.borrowed = int(time.time())  # - (86400*14)

    def __repr__(self):
        '''
        Represents the Issued status of the book asked for by the member of Library.
        Represents the Book_items details that is to be issued from the Library.
        ...

        Returns
        -------
        Formatted string: Contains the information about issue book. 

        '''
        return f"ISSUED_RES: {self.is_issued}, Book: {self.message}, Borrowed: {getDate(self.borrowed)}"


def getDate(borrowed):
    '''
    Returns timestamp of the day when book was issued to the member.
    ...
    Parameters
    ----------
            1. int : borrowed
                Epoch of the moment when the book was issued to the member
    '''
    timestamp = datetime.datetime.fromtimestamp(borrowed)
    return timestamp.strftime('%Y-%m-%d %H:%M')
