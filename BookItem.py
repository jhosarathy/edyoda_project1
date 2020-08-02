# -*- coding: utf-8 -*-
class BookItem:
    '''
    Class to create a copy of the book that is already in the catalog
    ...

    Attribute
    ---------
    isbn: str 
        The unique identity number for each copy of the book
    rack: str 
        Shelf where the book is placed in the physical library

    '''

    def __init__(self, book, isbn, rack):
        '''
        Constructs all the necessary attributes for the Book object
        ...
        Parameters
        ----------
        isbn: str 
            The unique identity number for each copy of the book
        rack: str 
            Shelf where the book is placed in the physical library
            
        '''
        self.book = book
        self.isbn = isbn
        self.rack = rack
        
