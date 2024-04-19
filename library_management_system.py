import book
import os

def main ():
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
    

def load_books(file_path):
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

def search_books(search_string, book_list): # option 1, check if search string matches in isbn, title, author or genre, return search list
    search_result = []
    lower_ss = search_string.lower()
    for book in book_list:
        genre = book.get_genre_name()
        if lower_ss in book.isbn.lower() or lower_ss in book.title.lower() or lower_ss in book.author.lower() or lower_ss in genre.lower():
            search_result.append(book)        
    return search_result

def borrow_book(book_list): # option 2
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

def print_menu():
    return

def find_book_by_isbn(isbn, book_list):
    pass

def return_book(book_list): # option 3
    pass

def add_book(book_list): # option 4
    pass

def remove_book(book_list): # option 5
    pass

def print_books(print_list): # option 6, 1
    pass

def save_books(book_list, file_path):
    pass


if __name__ == "__main__":
    main()
