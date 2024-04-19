

class Book:
    
    def __init__(self, isbn, title, author, genre, availability):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.availability = availability
        return
    

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author
    
    def get_isbn(self):
        return self.isbn
    
    def get_genre_name(self):
        genre_list = ["Romance", "Mystery", "Science Fiction", "Thriller", "Young Adult", "Children's Fiction", "Self-help", "Fantasy", "Historical Fiction", "Poetry"]
        return genre_list[self.genre]
    
    def get_availability(self):
        if self.availability:
            status = 'Available'
        else:
            status = 'Borrowed'
        return status

    def borrow_it(self):
        self.availability = False
        return

    def return_it(self):
        self.availability = True
        return

    def set_isbn(self, new_isbn):
        self.isbn = new_isbn
        return
    
    def set_title(self, new_title):
        self.title = new_title
        return
    
    def set_author(self, new_author):
        self.author = new_author
        return
    
    def set_genre(self, new_genre):
        self.genre = new_genre
        return

    def __str__(self):
        genre = self.get_genre_name()
        status = self.get_availability()
        result = f'{self.isbn:<14s} {self.title:<25s} {self.author:<25s} {genre:<20s} {status:<20s}'
        return result



