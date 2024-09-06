class Author:
    def __init__(self, name, biography):
        self.__name = name
        self.__biography = biography

    def name(self):
        return self.__name

    def biography(self):
        return self.__biography