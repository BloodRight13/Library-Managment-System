class Book:
    def __init__(self, title, author, isbn, publication_date, genre):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__publication_date = publication_date
        self.__genre = genre
        self.__is_borrowed = False

    def title(self):
        return self.__title
    
    def author(self):
        return self.__author
    
    def isbn(self):
        return self.__isbn
    
    def publication_date(self):
        return self.__publication_date

    def genre(self):
        return self.__genre

    def is_borrowed(self):
        return self.__is_borrowed

    def borrow(self):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            return True
        return False

    def return_book(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            return True
        return False
