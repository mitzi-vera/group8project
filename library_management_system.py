import book
import os

def main (): # mitzi
    print("Starting the system...")
    curr_dir = os.getcwd()
    file_name = input("Enter book catalog filename: ")
    file_path = os.path.join(curr_dir, file_name)
    if os.path.exists(file_path):
        book_list = load_books(file_path)
        print("Book catalog has been loaded.")
        selection = 'p' # placeholder value
        valid_selections = {"1" : "Search for books", "2" : "Borrow a book", "3" : "Return a book"} 
        heading = "\nReader's Guild Library - Main Menu"
        selection = print_menu(heading, valid_selections)
        while selection != '0':                    
            if selection == '2130':
                valid_selections.update({"4" : "Add a book", "5" : "Remove a book", "6" : "Print catalog"})
                heading = "\nReader's Guild Library - Librarian Menu"
            else:
                    if selection == '1': 
                        print("-- Search for Books --")
                        search_string = input("Enter Search Value: ")
                        search_result = search_books(search_string, book_list)
                        if len(search_result) == 0:
                            print("No matching books found.")
                        else:
                            print_books(search_result)
                    elif selection == '2':
                        print("\n-- Borrow a book --")
                        borrow_book(book_list)
                    elif selection == '3': 
                        print("\n-- Retun a book --")
                        return_book(book_list)
                    elif selection == '4': 
                        print("\n-- Add a book --")
                        book_list = add_book(book_list)
                    elif selection == '5': 
                        print("\n-- Remove a book --")
                        book_list = remove_book(book_list)
                    elif selection == '6': 
                        print_books(book_list)
            selection = print_menu(heading, valid_selections)

        save_books(book_list, file_path)
        print("-- Exit the system --")
        print("Book catalog has been saved.")
        print("Good Bye!")
    else:
        print("File does not exist. Goodbye!\n")
    
# this is a test push
def load_books(file_path): # mitzi
    book_list = []
    infile = open(file_path, 'r')
    line = infile.readline()
    while line != '':
        line_list = []
        line_list = line.strip().split(',')
        availability = line_list[4].upper().strip() == 'TRUE'
        book_list.append(book.Book(line_list[0],line_list[1],line_list[2],int(line_list[3]), availability))
        line = infile.readline()
    infile.close()
    return book_list


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

def search_books(search_string, book_list): # mitzi
    search_result = []
    lower_ss = search_string.lower()
    for book in book_list:
        genre = book.get_genre_name()
        if lower_ss in book.isbn.lower() or lower_ss in book.title.lower() or lower_ss in book.author.lower() or lower_ss in genre.lower():
            search_result.append(book)        
    return search_result

def borrow_book(book_list): # mitzi
    to_borrow = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    idx = find_book_by_isbn(to_borrow, book_list)
    if idx != -1:
        title = book_list[idx].get_title()
        if book_list[idx].get_availability() == "Available":
            book_list[idx].borrow_it()
            print(f'{title} with ISBN {to_borrow} successfully borrowed.')
        else:
            print(f'{title} with ISBN {to_borrow} is not currently available.')            
    else:
        print("No book found with that ISBN.")
    return

def print_menu(): # ayo
    return


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
def find_book_by_isbn(isbn, book_list): # riya
    for book_obj in book_list:
        if isbn == book_obj.get_isbn():
          return book_list.index(book_obj)
    return -1


def add_book(book_list): # riya
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

def remove_book(book_list): # riya
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    book_idx = find_book_by_isbn(book_list, isbn)
    
    if book_idx == -1:
        print("No book found with that ISBN.")
    else:
        print(f"'{book_list[book_idx].get_title()}' with ISBN {isbn} successfully removed.")
    del book_list[book_idx]


def save_books(book_list, file_path):def print_books(print_list): # option 6, 1
    print("{:<14s} {:<25s} {:<25s} {:<20s} {:<s}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    print("{:<14s} {:<25s} {:<25s} {:<20s} {:<s}".format("-"*14, "-"*25, "-"*25, "-"*20, "-"*12))
    for book in print_list:
        print(book)
    return

def save_books(book_list, file_path): #riya
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
