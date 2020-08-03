# -*- coding: utf-8 -*-
from Catalog import Catalog
from Book import Book
from BookItem import BookItem
from Book import BookIssue
import time


class User():
    '''
    A class to create an user of the library
    ...

    Attributes
    ----------
    name : str
        Name of the user
    location : str
        Resedential city of the User
    age: int
        Age of the User
    aadhar_id: str
        Address proof of the user
    catalog: instance of class Catalog

    Methods
    -------
    __init__(name, location, age, aadhar_id):
        Constructs all the necessary attributes for the Book object

    '''

    def __init__(self, name, location, age, aadhar_id):
        '''
        Constructs all the necessary attributes for the Book object
        ...

        Parameters
        ----------
        name : str
            Name of the user
        location : str
            Resedential city of the User
        age: int
            Age of the User
        aadhar_id: str
            Address proof of the user
        catalog: instance of class Catalog

        '''
        self.name = name
        self.location = location
        self.age = age
        self.aadhar_id = aadhar_id
        self.catalog = Catalog.instance()


class Member(User):
    '''
    Subclass of User class to create a Member of the library
    ...

    Attributes
    ----------
    id : str
        Identity card of the student
    fine : int
        Initially set to 0.
        Increases with delay in return of the book.
    issued : object of class dictionary
        Stores information of the issued book as key, value pairs.

    Refer base class for other inherited parameters

    Methods
    -------
    __init__(name, location, age, aadhar_id, id):
        Constructs all the necessary attributes for the Book object
    __repr__():
        Returns formatted string with information(name, location, id) of student.
    issueBook(book_name, days=10):
        Issues book to the member.
    returnBook(book_name):
        Returns the issued book and calculates the fine if applicable.
    extendBook(book_name, extend_by_days = 1):
        Extends the book date to avoid fine.
    payFine(rupees):
        Lets the member pay his/her fine for the previous book.
    displayAllBooks():
        Displays all the available books.

    '''

    def __init__(self, name, location, age, aadhar_id, id):
        '''
        Constructs all the necessary attributes for the Book object
        ...
        Parameters
        ----------
        id : str
            Identity card of the student
        fine : int
            Initially set to 0.
            Increases with delay in return of the book.
        issued : object of class dictionary
            Stores information of the issued book as key, value pairs.

        '''
        super().__init__(name, location, age, aadhar_id)
        self.id = id
        self.fine = 0
        self.issued = {}

    def __repr__(self):
        return f"{self.name}, {self.location}, {self.id}"

    # assume name is unique
    def issueBook(self, book_name, days=10):
        '''
        Issues book to the member.
        Removes BookItem object from book_item.
        Stores the particular issue's information as an object of BookIssue class.

        ...

        Parameters
        ----------
        book_name : str
            book name to be issued.
        days : int
            Number of days for which the book is issued.

        '''
        if book_name in self.issued:
            return BookIssue(False, f"{book_name} already issued", "", "", -1)

        if self.fine > 0:
            return BookIssue(False, f"{book_name} will be issued if existing fine is paid", "", "", -1)

        book = self.catalog.searchByName(book_name)
        result = None
        if len(book.book_item) > 0:
            isbn = book.book_item[0].isbn
            rack = book.book_item[0].rack
            self.catalog.removeBookItem(book.name, isbn)
            msg = f"(Book: {book.name}, Author: {book.author}, ISBN: {isbn}) issued for {days} days"
            result = BookIssue(True, msg, isbn, rack, days)
            self.issued[book.name] = result
            book.updateBorrowedCount(1)
        else:
            result = BookIssue(False, "Book not available", "", "", -1)
        return result

    # assume name is unique
    def returnBook(self, book_name):
        '''
        Returns the issued book and calculates the fine if applicable.
        ...

        Parameters
        ----------
        book_name : str
            book name to be issued.

        Returns
        -------
        Formatted string: Return status and book's detail.
                          Fine to be paid.

        '''
        if book_name in self.issued:
            # Fetch borrow details
            bookIssued = self.issued[book_name]
            book = self.catalog.searchByName(book_name)
            isbn = bookIssued.isbn
            rack = bookIssued.rack
            # Calculate Fine
            numDays = (time.time() - bookIssued.borrowed) // 86400
            curFine = 0
            del self.issued[book_name]
            # print(f"NUM_DAYS_RETURN: {numDays} {bookIssued.days}")
            if numDays > 10:
                curFine = (numDays - bookIssued.days) * 10
            if curFine > 0:
                self.fine = self.fine + curFine
            self.catalog.addBookItem(book_name, isbn, rack)
            book.updateBorrowedCount(-1)
            return f"RETURN_SUCCESS: (BookName {book_name}, ISBN {isbn}, Rack {rack}, Fine for book {curFine}, Total Fine {self.fine}) returned successfully"
        return f"RETURN_FAILURE: {book_name} not borrowed by you"

    # assume name is unique
    def extendBook(self, book_name, extend_by_days=1):
        '''
        Extends the book date to avoid fine.
        ...

        Parameters
        ----------
        book_name : str
            name of the book
        extend_by_days : int
            No.of.days the member wants to extend the book from the actual day.

        Returns
        -------
        Formatted string : With status message and the book name.

        '''
        if book_name in self.issued:
            bookIssued = self.issued[book_name]
            bookIssued.days += extend_by_days
            return f"EXTEND_SUCCESS: (Book {book_name}, ISBN {bookIssued.isbn}, Rack {bookIssued.rack}) extended by {extend_by_days}"
        else:
            return f"EXTEND_FAILURE: {book_name} not borrowed by you"

    def payFine(self, rupees):
        '''
        Lets the member pay his/her fine for the previous book.
        ...

        Parameters
        ----------
        rupees : int
            The amount, member intends to pay against his/her fine.

        Returns
        -------
        Formatted string: Status of payment and balance if any. 

        '''
        if self.fine > 0:
            if rupees <= self.fine:
                self.fine = self.fine - rupees
                return f"PAYING_FINE_SUCCESS: {self.name}'s fine is now, {self.fine} Rs."
            else:
                self.fine = 0
                balance = rupees - self.fine
                return f"PAYING_FINE_SUCCESS: {self.name}'s fine is now, {self.fine} Rs and balance is {balance}"
        return f"PAYING_FINE_FAILURE: {self.name}'s fine is 0 Rs"

    def displayAllBooks(self):
        '''
        Prints the total count of different books available in Library for issue.
        Prints all the available books.
        Prints the total count of all the books including the copies available in Library for issue.
        ...

        '''
        return self.catalog.displayAllBooks()


class Librarian(User):
    '''
    Subclass of User class to create a Librarian of the library
    ...

    Parameters
    ----------
    emp_id : str
        Identity card of the student

    Refer base class for other inherited parameters

    Methods
    -------
    __init__(name, location, age, aadhar_id, emp_id):
        Constructs all the necessary attributes for the Book object
    __repr__():
        Returns formatted string with information(name, location, id) of librarian.
    addBook(book_name,author,publish_date,pages):
        Creates a Book object and appends it to the books list
    addBookItem(book_name, isbn,rack):
        Adds a new copy of the already existing book to the book_item
    removeBook(name):
        Removes a book from the books list.
    removeBookItemFromCatalog(name, isbn):
        Removes a book copy from book_item.
    displayAllBooks():
        Displays all the available books.

    '''

    def __init__(self, name, location, age, aadhar_id, emp_id):
        '''

        Constructs all the necessary attributes for the Book object
        ...
        Parameters
        ----------
        emp_id : str
            Identity card of the Librarian

        '''
        super().__init__(name, location, age, aadhar_id)
        self.emp_id = emp_id

    def __repr__(self):
        '''
        Returns formatted string with information(name, location, id) of librarian.
        ...

        '''
        return f"{self.name}, {self.location}, {self.emp_id}"

    def addBook(self, book_name, author, publish_date, pages):
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
        return self.catalog.addBook(book_name, author, publish_date, pages)

    def addBookItem(self, book_name, isbn, rack):
        '''
        Adds a new copy (BookItem object) of the already existing book to the book_item
        ...
        Parameters
        ----------
        book_name : string
            Name of the book to which we've to add the ISBN
        isbn : string
            The unique identity number for each copy of the book
        rack: string
            Shelf where the book is placed in the physical library

        Returns
        -------
        Status of the method. (If added or not with reason)

        '''
        return self.catalog.addBookItem(book_name, isbn, rack)

    def removeBook(self, book_name):
        '''
        Removes a book from the books list.
        ...
        Parameters
        ----------
        book_name : str
            Name of the Book

        '''
        b = self.catalog.searchByName(book_name)
        if b.borrowed != 0:
            return f"REMOVE_FAILURE: {book_name} has been issued to {b.borrowed} borrowers. Cannot remove now."
        res = self.catalog.removeBook(book_name)
        return res

    def removeBookItemFromCatalog(self, book_name, isbn):
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
        self.catalog.removeBookItem(book_name, isbn)

    def displayAllBooks(self):
        '''
        Prints the total count of different books available in Library for issue.
        Prints all the available books.
        Prints the total count of all the books including the copies available in Library for issue.
        ...

        '''
        return self.catalog.displayAllBooks()
