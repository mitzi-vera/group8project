

class Book:
    
    def __init__(self, isbn, title, author, genre, availability):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__availability = availability
        return
    

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author
    
    def get_isbn(self):
        return self.__isbn
    
    def get_genre(self):
        return self.__genre
    
    def get_genre_name(self):
        genre_list = ["Romance", "Mystery", "Science Fiction", "Thriller", "Young Adult", "Children's Fiction", "Self-help", "Fantasy", "Historical Fiction", "Poetry"]
        return genre_list[self.__genre]
    
    def get_availability(self):
        if self.__availability:
            status = 'Available'
        else:
            status = 'Borrowed'
        return status

    def borrow_it(self):
        self.__availability = False
        return

    def return_it(self):
        self.__availability = True
        return

    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn
        return
    
    def set_title(self, new_title):
        self.__title = new_title
        return
    
    def set_author(self, new_author):
        self.__author = new_author
        return
    
    def set_genre(self, new_genre):
        self.__genre = new_genre
        return

    def __str__(self):
        genre = self.get_genre_name()
        status = self.get_availability()
        isbn = self.get_isbn()
        title = self.get_title()
        author = self.get_author()
        result = f'{isbn:<14s} {title:<25s} {author:<25s} {genre:<20s} {status:<20s}'
        return result



