class Book:
    GENRE_LIST = ["Romance", "Mystery", "Science Fiction", "Thriller", "Young Adult", "Children's Fiction", "Self-help", "Fantasy", "Historical Fiction", "Poetry"]
    
    def __init__(self, isbn, title, author, genre, availability):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__availability = availability
    
    def get_title(self):
      return self.__title

    def get_author(self):
      return self.__author
    
    def get_isbn(self):
      return self.__isbn
    
    def get_genre(self):
      return self.__genre
    
    def get_genre_name(self):
      return Book.GENRE_LIST[self.__genre]

    def get_available(self):
      return self.__availability
    
    def get_availability(self):
      if self.__availability: 
        return "Available"
      else:
        return "Borrowed"

    def borrow_it(self):
      self.__available = False

    def return_it(self):
      self.__available = True

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
      return f"{self.__isbn:<14s} {self.__title:<25s} {self.__author:<25s} {self.get_genre_name():<20s} {self.get_availability()}"






