# -*- coding: utf-8 -*-
from Book import Book
from Catalog import Catalog
from User import Member, Librarian
from System import System
from ImportFile import import_data
import sys

# 1. Create library object
system = System.instance()
print(import_data(system))
# sys.exit()

# 2. Register Librarians: Library System prevents duplicate aadhar numbers in registry
res1 = system.registerLibrarian("Harry Potter", "Bangalore", 30, "aadhar_1", "empl_1")
if res1["registration_status"] is True:
    print(f"NEW_LIBRARIAN: {system.getLibrarian('aadhar_1').__repr__()}")
else:
    print(f"NEW_LIBRARIAN_ERROR: {res1}")

res2 = system.registerLibrarian("Hermione Granger", "Bangalore", 29, "aadhar_2", "empl_2")
if res2["registration_status"] is True:
    print(f"NEW_LIBRARIAN: {system.getLibrarian('aadhar_2').__repr__()}")
else:
    print(f"NEW_LIBRARIAN_ERROR: {res2}")

# 3. Librarian adds books and book items
l1 = system.getLibrarian("aadhar_1")
if l1:
    # Add book1
    b1 = l1.addBook('Shoe Dog', 'Phil Knight', '2015', 312)
    # Add book items to book1
    l1.addBookItem('Shoe Dog', '123hg', 'H1B2')
    l1.addBookItem('Shoe Dog', '124hg', 'H1B4')
    l1.addBookItem('Shoe Dog', '125hg', 'H1B5')

    # Add book2
    b2 = l1.addBook('Moonwalking with Einstien', 'J Foer', '2017', 318)
    # Add book items to book2
    l1.addBookItem('Moonwalking with Einstien', '463hg', 'K1B2')
else:
    print(f"LIBRARIAN_NOT_FOUND: aadhar_1")


# 4. Register Members
res1 = system.registerMember("Neville Longbottom", "Bangalore", 22, "aadhar_3", "student_1")
if res1["registration_status"] is True:
    print(f"NEW_MEMBER: {system.getMember('aadhar_3').__repr__()}")
else:
    print(f"NEW_MEMBER_ERROR: {res2}")

# 5. Member borrows book
m1 = system.getMember("aadhar_3")
if m1:
    bookIssueRes = m1.issueBook("Moonwalking with Einstien")
    print(bookIssueRes)
    bookIssueRes1 = m1.issueBook("Moonwalking with Einstien")
    print(bookIssueRes1)
else:
    print(f"MEMBER_NOT_FOUND: aadhar_3")

# 6. Librarian removes books: Should Fail [Since book has been borrowed]
res = l1.removeBook("Moonwalking with Einstien")
print(res)

# 7. Member extends no.of.days of book issue
res = m1.extendBook("Shoe Dog")
print(res)

#8. Member extends a book
res = m1.extendBook("Moonwalking with Einstien", 2)
print(res)

# 9. Member returns book
res = m1.returnBook("Moonwalking with Einstien")
print(res)

# 10. Member borrows the returned book again
bookIssueRes = m1.issueBook("Moonwalking with Einstien")
print(bookIssueRes)

# 11. Member pays fine
res = m1.payFine(10)
print(res)

# 12. Librarian removes books: Should Succeed [Since book has been returned]
res = l1.removeBook("Moonwalking with Einstien")
print(res)

# 13. Librarian views updated catalog of the library with all the available
print("LIBRARIAN_VIEW")
l1.displayAllBooks()

# 14. Member views all the available books
print("MEMBER_VIEW")
m1.displayAllBooks()

