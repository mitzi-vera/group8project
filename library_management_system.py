# Title: Library Management System
# Date: April 19, 2024
# Authors: Riya Johari, Ayomide Anuoluwapo Adewunmi, Mitzi Vera Escartin
# Prepared for Doug Shier
# CPRG 216 - Object Oriented Programming 1
# This Library Management system efficiently handles library operations. It loads book data from CSV at start-up and offers users main menu functions: Search books, Borrow books, Return books, and Exit the program. For librarians, a secret passcode of 2130 unlocks some additional options: Add books, Remove books, and Print catalog. All changes are saved to CSV upon shut-down. This streamlined system ensures seamless library management for both users and librarians.

# importing book.py and os module
import book
import os

def main ():
    print("Starting the system...")
    curr_dir = os.getcwd()
    file_name = input("Enter book catalog filename: ")
    # Loop continues on as long as the user does not enter a valid file path and name
    while not os.path.exists(os.path.join(curr_dir, file_name)):
        file_name = input("File not found. Re-enter book catalog file name: ")

    file_path = os.path.join(curr_dir, file_name)
    # Initialising book_list
    book_list = []
    # Calling load_books() function and loading book_list with book objects
    count_books = load_books(file_path, book_list)
    print("Book catalog has been loaded.")
    selection = 'p' # placeholder value
    # Initialising valid selections dictionary and a header
    valid_selections = {"1" : "Search for books", "2" : "Borrow a book", "3" : "Return a book"} 
    heading = f"\nReader's Guild Library - Main Menu \n{"=" * 34}"
    # Loop continues on until user ends the program by inputing 0 as a selection
    while selection != '0':    
        # Calling print_menu() function
        selection = print_menu(heading, valid_selections)    
        # Secret library menu options unlocked with a special code of 2130          
        if selection == '2130':
            # Updating valid_selections dict by adding new options
            valid_selections.update({"4" : "Add a book", "5" : "Remove a book", "6" : "Print catalog"})
            heading = f"\nReader's Guild Library - Librarian Menu \n{"=" * 39}"
        else:
                # search_books()
                if selection == '1': 
                    print("\n-- Search for Books --")
                    search_string = input("Enter Search Value: ")
                    search_result = search_books(search_string, book_list)
                    if len(search_result) == 0:
                        print("No matching books found.")
                    else:
                        print_books(search_result)
                # borrow_books()
                elif selection == '2':
                    print("\n-- Borrow a book --")
                    borrow_book(book_list)
                # return_books()
                elif selection == '3': 
                    print("\n-- Return a book --")
                    return_book(book_list)
                # add_books()
                elif selection == '4': 
                    print("\n-- Add a book --")
                    add_book(book_list)
                # remove_books()
                elif selection == '5': 
                    print("\n-- Remove a book --")
                    remove_book(book_list)
                # print_books()
                elif selection == '6': 
                    print_books(book_list)

    # Saving data and copying data from book_list to books.csv file
    save_books(book_list, file_path)
    # Exit message
    print("\n-- Exit the system --")
    print("Book catalog has been saved.")
    print("Good Bye!")

def load_books(file_path, book_list):
    """
    Load books from a CSV file into a list.
    
    Parameters:
    book_list (list): An empty list to store the loaded books.
    csv_file_path (str): The pathname to the existing CSV file containing book data.
    
    Returns:
    int: The number of books loaded into the list.
    
    Receives an empty list and pathname to an existing CSV file.
    Iterates over each line (i.e., book) in the file, parsing the attribute values into separate variables.
    Creates Book objects from each set of attributes and adds them one-by-one onto the list.
    """

    infile = open(file_path, 'r')
    line = infile.readline()
    while line != '':
        line_list = []
        line_list = line.strip().split(',')
        available = line_list[4].capitalize() == 'True'
        book_list.append(book.Book(line_list[0],line_list[1],line_list[2],int(line_list[3]), available))
        line = infile.readline()
    infile.close()
    return len(book_list)

def print_menu(heading, valid_selections):
    """
    Display a menu heading and options, prompt user for selection, and return valid selection.

    Parameters:
    menu_heading (str): The heading for the menu.
    menu_options (dict): A dictionary containing menu options as keys and their descriptions as values.

    Returns:
    str: The user's valid selection from the menu.

    Receives menu heading (string) and menu options (dictionary).
    Displays the heading and menu options passed in.
    Inputs selection from the user until a valid selection is entered.
    """

    print(heading)
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

def search_books(search_string, book_list):
    """
    Search for books based on a search string in ISBN, title, author, or genre.

    Parameters:
    book_list (list): The list of books to search through.
    search_string (str): The string to search for in book attributes.

    Returns:
    list: The list of books matching the search criteria.

    Before calling this function, input search string from the user.
    Receives a book list and a search string.
    Iterates through the list of books and checks if the search string appears in ISBN, title, author, or genre name.
    If any match is found, the book is added to the search result list.
    After calling this function, call print_books() passing to it the search result list.
    """

    search_result = []
    lower_ss = search_string.lower()
    for book in book_list:
        genre = book.get_genre_name()
        if lower_ss in book.get_isbn().lower() or lower_ss in book.get_title().lower() or lower_ss in book.get_author().lower() or lower_ss in genre.lower():
            search_result.append(book)        
    return search_result

def borrow_book(book_list):
    """
    Borrow a book from the library.

    Parameters:
    book_list (list): The list of books available in the library.

    Receives a book list.
    Inputs an ISBN from the user and calls find_book_by_isbn().
    If an index to a matching book was returned and that book is currently available, invokes the book's borrow_it() method.
    Otherwise, displays an appropriate message.
    """

    to_borrow = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    idx = find_book_by_isbn(to_borrow, book_list)
    if idx != -1:
        title = book_list[idx].get_title()
        if book_list[idx].get_available():
            book_list[idx].borrow_it()
            print(f'{title} with ISBN {to_borrow} successfully borrowed.')
        else:
            print(f'{title} with ISBN {to_borrow} is not currently available.')            
    else:
        print("No book found with that ISBN.")
    return

def return_book(book_list): 
    """
    Return a borrowed book to the library.

    Parameters:
    book_list (list): The list of books available in the library.

    Receives a book list.
    Inputs an ISBN from the user and calls find_book_by_isbn().
    If an index to a matching book was returned and that book is currently borrowed,
    invokes the book class's return_it() method.
    Otherwise, displays an appropriate message.
    """

    to_return = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    idx = find_book_by_isbn(to_return, book_list)
    if idx != -1:
        title = book_list[idx].get_title()
        if not book_list[idx].get_available():
            book_list[idx].return_it()
            print(f'{title} with ISBN {to_return} successfully returned.')  
        else:
            print(f'{title} with ISBN {to_return} is not currently borrowed.')
    else:
        print("No book found with that ISBN.")
    return

def find_book_by_isbn(isbn, book_list):
    """
    Find a book by matching ISBN.

    Parameters:
    book_list (list): The list of books available in the library.
    isbn (str): The ISBN of the book to be returned.

    Receives a book list and an ISBN.
    Iterates through the list of books and compares the ISBN parameter to each book's ISBN.
    Iteration stops when an exact match is found or when the end of the list is reached.
    Returns the index of the matching book or -1 if none found.
    """

    for book_obj in book_list:
        if isbn == book_obj.get_isbn():
          return book_list.index(book_obj)
    return -1

def add_book(book_list):
    """
    Add a new book to the library.

    Parameters:
    book_list (list): The list of books available in the library.

    Receives a book list.
    Inputs ISBN, title, author, and genre name from the user.
    Genre name is validated - it must be one of the names listed earlier in the description of get_genre_name() -
    and translated into its integer value.
    Creates a new instance of Book and appends it to the list.
    """

    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author name: ")
    
    genre = input("Enter genre: ")
    while genre not in book.Book.GENRE_LIST:
        print("Invalid genre. Choices are: ", end="")
        for valid_genre in book.Book.GENRE_LIST:
          print(valid_genre, end=", ")
        genre = input("\nEnter genre: ")
    
    genre_no = book.Book.GENRE_LIST.index(genre)
    available = True
    book_obj = book.Book(isbn, title, author, genre_no, available)
    book_list.append(book_obj)
    print(f"'{title}' with ISBN {isbn} successfully added.")

def remove_book(book_list):
    """
    Remove a book from the library.

    Parameters:
    book_list (list): The list of books available in the library.

    Receives a book list.
    Inputs an ISBN from the user and calls find_book_by_isbn().
    If an index to a matching book was returned, removes the book from the list.
    Otherwise, displays an appropriate message.
    """

    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    book_idx = find_book_by_isbn(isbn, book_list)
    
    if book_idx == -1:
        print("No book found with that ISBN.")
    else:
        print(f"'{book_list[book_idx].get_title()}' with ISBN {isbn} successfully removed.")
        book_list.pop(book_idx)
       
def print_books(print_list): 
    """
    Print information about the books in the library.

    Parameters:
    book_list (list): The list of books available in the library.

    Receives a book list.
    Displays a book information heading, then iterates through the book list displaying each Book object on a separate line.
    """
      
    print("{:<14s} {:<25s} {:<25s} {:<20s} {:<s}".format("ISBN", "Title", "Author", "Genre", "Availability"))
    print("{:<14s} {:<25s} {:<25s} {:<20s} {:<s}".format("-"*14, "-"*25, "-"*25, "-"*20, "-"*12))
    for book in print_list:
        print(book)
    return

def save_books(book_list, file_path):
    """
    Save book information to a CSV file.

    Parameters:
    book_list (list): The list of books available in the library.
    csv_file_path (str): The pathname to the CSV file to save the book information.

    Receives a book list and a pathname to a CSV file.
    Iterates over the list, formatting a comma-separated string containing each book's attribute values.
    Writes each string as a separate line to the file.
    Returns the number of books saved to the file.
    """

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
    book_file.close()
    return num_books

if __name__ == "__main__":
    main()
