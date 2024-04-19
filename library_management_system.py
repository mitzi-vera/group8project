import book
import os

def main ():
    pass
    

def load_books(file_path):
    pass

def print_menu(librarian_mode):
    pass

def search_books(search_string, book_list): # option 1
    pass

def borrow_book(book_list): # option 2
    pass

def find_book_by_isbn(isbn, book_list):
    for book_obj in book_list:
        if isbn == book_obj.get_isbn():
          return book_list.index(book_obj)
    return -1

def add_book(book_list): # option 4
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author name: ")
    
    genre = input("Enter genre: ")
    while genre not in book.Book.GENRE:
        print("Invalid genre. Choices are: ", end="")
        for valid_genre in book.Book.GENRE:
          print(valid_genre, end=", ")
        genre = input("\nEnter genre: ")
    
    genre_no = book.Book.GENRE.index(genre)
    available = True
    book_obj = book.Book(isbn, title, author, genre_no, available)
    book_list.append(book_obj)
    print(f"'{title}' with ISBN {isbn} successfully added.")

def remove_book(book_list): # option 5
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    book_idx = find_book_by_isbn(book_list, isbn)
    
    if book_idx == -1:
        print("No book found with that ISBN.")
    else:
        print(f"'{book_list[book_idx].get_title()}' with ISBN {isbn} successfully removed.")
    del book_list[book_idx]

def print_books(print_list): # option 6, 1
    pass

def save_books(book_list, file_path):
    book_file = open(file_path, "w")
    num_books = 0
    
    for book_obj in book_list:
        isbn = book_obj.get_isbn()
        title = book_obj.get_title()
        author = book_obj.get_author()
        genre = book_obj.get_genre()
        available = book_obj.get_available()
        
        line = f"{isbn},{title},{author},{genre},{available}\n"
        book_file.write(line)
        
        num_books += 1
    
    return num_books


if __name__ == "__main__":
    main()
