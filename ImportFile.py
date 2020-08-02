import argparse
import sys
import pathlib


def import_data(system):
    '''
    Imports librarians, members, books and bookitem from tsv files.
    ....
    Parameters
    ----------
    system : object of system class
        This object is used to register members and librarians

    Returns
    -------
    List : Contains 2 items viz. bool and str.
        The bool item represents whether this operation was successful or not.
        The str item represents the error message or success message.
    '''
    parser = argparse.ArgumentParser(description='Library management system')
    parser.add_argument('--books-file', help='Books file')
    parser.add_argument('--book-items-file', help='Book items file')
    parser.add_argument('--users-file', help='Users file')
    librarian = None
    args = parser.parse_args()
    if (not is_empty(args.books_file)) or (not is_empty(args.book_items_file)) or (not is_empty(args.users_file)):
        if is_empty(args.book_items_file) or is_empty(args.users_file) or is_empty(args.books_file):
            errStr = "All of --books-file and --book-items-file and --users-file have to be set together"
            return [False, errStr]
        file = pathlib.Path(args.books_file)
        if not file.exists():
            return [False, f"{args.books_file} does not exist"]
        file = pathlib.Path(args.book_items_file)
        if not file.exists():
            return [False, f"{args.book_items_file} does not exist"]
        file = pathlib.Path(args.users_file)
        if not file.exists():
            return [False, f"{args.users_file} does not exist"]

        numMembers = 0
        numLibrarians = 0
        numBooks = 0
        numBookItems = 0
        # Read users-file TSV file    
        with open(args.users_file, 'r') as f:
            for line in f:
                line = line.strip()    
                tokens = line.split("\t")
                # name, location, age, aadhar_id, emp_id, user_type
                if tokens[5] == "LIBRARIAN":
                    res = system.registerLibrarian(tokens[0], tokens[1], int(tokens[2]), tokens[3], tokens[4])
                    print(f"{tokens[0]}\t{res}")
                    librarian = system.getLibrarian(tokens[3])
                    if res["registration_status"]:
                        numLibrarians += 1
                else:
                    res = system.registerMember(tokens[0], tokens[1], int(tokens[2]), tokens[3], tokens[4])
                    if res["registration_status"]:
                        numMembers += 1
                    print(f"{tokens[0]}\t{res}")
        if librarian is None:
            return [False, f"{args.users_file} has 0 librarians. Cannot add books without librarian"]
        with open(args.books_file, 'r') as f:
            for line in f:
                line = line.strip() 
                tokens = line.split("\t")
                # name, author, publish_date, pages, book_item
                b = librarian.addBook(tokens[0], tokens[1], tokens[2], int(tokens[3]))
                if b is not None:
                    numBooks += 1
                print(f"BOOK_ADDED: {b}")
        with open(args.book_items_file, 'r') as f:
            for line in f:
                line = line.strip() 
                tokens = line.split("\t")
                # name, author, publish_date, pages, book_item
                res = librarian.addBookItem(tokens[0], tokens[1], tokens[2])
                if res.find("SUCCESS") != -1:
                    numBookItems += 1
                print(f"{res}")
        return [True, f"Imported ({numLibrarians} Librarians, {numMembers} Members, {numBooks} Books, {numBookItems} BookItems)"]


def is_empty(d):
    '''
    Returns whether the input string is empty or not.
    ----
    Parameter
    ---------
    d : str

    Returns
    -------
    Bool 
     
    '''
    if (not d) or d == "":
        return True
    return False
