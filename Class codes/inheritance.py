class LibraryItem:
    def __init__(self, title, subject, status):
        self.title, self.subject, self.status = title, subject, status


    def booking(self):
        return f'your booking of {self.title} was succesful'

class Book(LibraryItem):
    def __init__(self, ISBN, authors, title, subject, status):
        self.ISBN = ISBN
        self.authors = authors
        super().__init__(title, subject, status)

    def booking(self):
        return f'your booking of {self.title} was succesful'

class Magazine(LibraryItem):
    def __init__(self, journalName, volume, status):
        self.journalName = journalName
        self.volume = volume
        super().__init__(status)

    def booking(self):
        return f'your booking of {self.title} was succesful'

class CD(LibraryItem):
    def __init__(self, title, status):
        super().__init__(title, status)

    def __str__(self):
        return "You cant book CD's"

self.status = "available" or "occupied"
