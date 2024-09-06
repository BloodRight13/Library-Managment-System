class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id
        self.__borrowed_books = []

    def name(self):
        return self.__name

    def library_id(self):
        return self.__library_id

    def borrowed_books(self):
        return self.__borrowed_books

    def borrow_book(self, book):
        if book.borrow():
            self.__borrowed_books.append(book.title)
            return True
        return False

    def return_book(self, book):
        if book.return_book():
            self.__borrowed_books.remove(book.title)
            return True
        return False
