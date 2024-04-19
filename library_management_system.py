import book
import os

def main ():
    pass
    
# this is a test push
def load_books(file_path):
    pass

def print_menu(heading, valid_selections):
    print(heading)
    print('='*34)
    for key in valid_selections:
        print(key + "." + valid_selections[key])
    print("0. Exit the system")
    invalid_selection = True
    while invalid_selection:
        selection = input("Enter your selection: ")
        if selection in valid_selections or selection in ['0', '2130']:
            invalid_selection = False
        else:    
            print("Invalid option.")
    return selection
    
# this is a 2nd test
def search_books(search_string, book_list): # option 1
    pass

def borrow_book(book_list): # option 2
    pass

def find_book_by_isbn(isbn, book_list):
    pass

def return_book(book_list):def return_book(book_list): # option 3
    to_return = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    idx = find_book_by_isbn(to_return, book_list)
    if idx != -1:
        title = book_list[idx].get_title()
        print(book_list[idx].get_availability())
        if book_list[idx].get_availability() == 'Borrowed':
            book_list[idx].return_it()
            print(f'{title} with ISBN {to_return} successfully returned.')  
        else:
    pass

def add_book(book_list): # option 4
    pass

def remove_book(book_list): # option 5
    pass

def print_books(print_list): # option 6, 1
    pass

def save_books(book_list, file_path):def print_books(print_list): # option 6, 1
    print("{:<14s} {:<25s} {:<25s} {:<20s} {:<s}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    print("{:<14s} {:<25s} {:<25s} {:<20s} {:<s}".format("-"*14, "-"*25, "-"*25, "-"*20, "-"*12))
    for book in print_list:
        print(book)
    return
    pass


if __name__ == "__main__":
    main()
