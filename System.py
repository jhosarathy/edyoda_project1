from Singleton import Singleton
from Catalog import Catalog
from User import Member, Librarian


class System(Singleton):

    '''
    A class to represent a Library
    ...

    Attribute
    ---------

    members : object of class dictionary
        Dictionary of Member objects of the library as keys and their attributes as values.
    librarians : object of class dictionary
        Dictionary of Librarian objects of the library as keys and their attributes as values.

    Methods
    -------

    __init__():
        Constructs all the necessary attributes for the Book object
    registerMember(name, location, age, aadharId, studentId):
        Verifies the aadhar_id and checks if it already is used to create a member.
        Registers a member.
    getMember(aadharId):
        Returns Member object 
    getMemberByName(name):
        Returns Member object
    registerLibrarian(name, location, age, aadharId, empId):
        Verifies the aadhar_id and checks if it already is used to create a librarian.
        Registers a Librarian.
    getLibrarian(self, aadharId):
        Returns Librarian object
    getLibrarianByName(self, name):
        Returns Librarian object
    '''

    def __init__(self):
        '''
        Constructs all the necessary attributes for the Book object.
        ...

        Parameters
        ----------
        members : object of class dictionary
            Dictionary of Member objects of the library as keys and their attributes as values.
        librarians : object of class dictionary
            Dictionary of Librarian objects of the library as keys and their attributes as values.

        '''
        self.members = {}
        self.librarians = {}

    def registerMember(self, name, location, age, aadharId, Id):
        '''
        Verifies the aadhar_id and checks if it already is used to create a member.
        Registers a member.
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
        Id : str
            Identity card of the student/employee

        Returns
        -------
        A dictionary: With "Status" as key and Bool as value.

        '''
        res = {"registration_status": True}
        if aadharId in self.members:
            res = {"registration_status": False,
                   "message": f"{aadharId} is already a member"}
            return res

        self.members[aadharId] = Member(name, location, age, aadharId, Id)
        return res

    def getMember(self, aadharId):
        '''
        Returns Member object matching with the aadharId passed as arguement.
        ...
        Attribute
        ---------
        aadhar_id: str
            Address proof of the user

        Returns
        -------
        Member object

        '''
        return self.members[aadharId]

    def getMemberByName(self, name):
        '''
        Returns Member object if the arguement passed and object.arguement valids.
        ...

        Attribute
        ---------
        name : str
            Name of the user

        Returns
        -------
        Member object

        '''
        for m1 in self.members.values():
            if m1.name == name:
                return m1
        return None

    def registerLibrarian(self, name, location, age, aadharId, empId):
        '''
        Verifies the aadhar_id and checks if it already is used to create a librarian.
        Registers a librarian.
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
        empID : str
            Identity card of the employee

        Returns
        -------
        A dictionary: With "Status" as key and Bool as value.

        '''
        res = {"registration_status": True}
        if aadharId in self.librarians:
            res = {"registration_status": False,
                   "message": f"{aadharId} is already a librarian"}
            return res
        if aadharId in self.members:
            res = {"registration_status": False,
                   "message": f"{aadharId} is a student. Only employees can become librarians"}
            return res

        self.librarians[aadharId] = Librarian(
            name, location, age, aadharId, empId)
        return res

    def getLibrarian(self, aadharId):
        '''
        Returns Librarian object if the arguement passed and object.arguement valids.
        ...

        Attribute
        ---------
        aadhar_id: str
            Address proof of the user

        Returns
        -------
        Librarian object

        '''
        return self.librarians[aadharId]

    def getLibrarianByName(self, name):
        '''
        Returns Librarian object if the arguement passed and object.arguement valids.
        ...

        Attribute
        ---------
        name : str
            Name of the user

        Returns
        -------
        Librarian object

        '''
        for li in self.librarians.values():
            if li.name == name:
                return li
        return None
