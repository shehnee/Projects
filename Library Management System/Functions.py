'''
Author : Cheng Sheh Nee
Admin No / Grp : 234745J / AA2301
'''

# date and time
import datetime

# multiple dict in a list (from the qn)
library = [
    {"isbn": "978-0134846019", "title": "Data Analytics with Spark Using Python", "type": "Paper Back", "quantity": 6},
    {"isbn": "978-0133316032", "title": "Children's Reading", "type": "eBook", "quantity": 3},
    {"isbn": "978-1292100142", "title": "Global Marketing, 7th Edition", "type": "eBook", "quantity": 8},
    {"isbn": "978-1587147029", "title": "CCNA Cyber Ops SECFND #210-250 Official Cert Guide", "type": "Hard Cover", "quantity": 5},
    {"isbn": "0306406152", "title": "Learn Data Analytics in 100 days", "type": "Paper Back", "quantity": 10}
]

borrowedCount = {}
borrowedBooks = []

# a fine of $0.50 per day for overdue books
finePerDay = 0.50

# log in function
def LogIn():
    print("--- WELCOME TO THE LIBRARY MANAGEMENT SYSTEM ---")
    username = input("Username: ")
    password = input("Password: ")

    # valid username and password
    validUsername = "Administrator"
    validPassword = "Pa$$w0rd"

    # verify the username
    if username == validUsername:
        # verify the password
        if password == validPassword:
            print("Login successful!")
            return True
        # error message for incorrect password
        else:
            print("Password is incorrect. Please try again.")
    # error message for invalid username
    else:
        print("Invalid username. Please enter a valid username.")

# function 1 - Add New Book
def AddNewBook():
    # only 3 types of books are allowed to store in the program
    bookTypes = ["Hard Cover", "Paper Back", "eBook"]

    # while loop as we do not know how many times to repeat
    while True:
        # user may quit this function
        isbn = input("Please enter the ISBN of the book. (Enter '0' to exit): ")
        if isbn.lower() == '0':
            return  # exit the function
        # check if the ISBN already exists in the library
        if any(book['isbn'] == isbn for book in library):
            print("A book with the same ISBN already exists in the library.\nPlease update the information of the existing book instead.")
            break

        # validation for ISBN (else statement: prompt error if it is invalid)
        if isbnValidation(isbn):
            bookTitle = input("Please enter the title of the book: ")

            # validation for Type of Book
            while True:
                bookType = input("Please enter the type of book with the following types (Hard Cover, Paper Back, eBook): ")
                if bookType in bookTypes:
                    break
                # prompt error if the book type is invalid (the 3 types)
                else:
                    print("Invalid book type. Please choose from the following: Hard Cover, Paper Back, or eBook.")

            # information for quantity
            while True:
                try:
                    quantity = int(input("Please enter the quantity of the book: "))
                    if quantity <= 0:
                        print("Quantity cannot be less than one. Please enter a positive number.")
                    else:
                        break
                except ValueError:
                    print("Invalid quantity. Please enter a valid number for the quantity of the book.")

            # gather all the information
            newBook = {"isbn": isbn, "title": bookTitle, "type": bookType, "quantity": quantity}
            # store information in the library
            library.append(newBook)
            # confirmation to provide positive feedback that book added successfully
            print("Book has added successfully! You may view the summary in the library.")
            break

        # error prompted for invalid ISBN
        else:
            print("Invalid ISBN. Please enter a valid ISBN.")

# function 2 - Update Existing Book
def UpdateExistingBook():
    bookTypes = ["Hard Cover", "Paper Back", "eBook"]

    while True:
        # get the ISBN of the book that user wishes to update information
        isbnUpdate = input("Please enter the ISBN of the book you wish to update (enter '0' to exit): ")
        # user may quit
        if isbnUpdate.lower() == '0':
            return  # exit the function

        # find all the relevant information with the given ISBN (using index)
        # initialise the index
        indexUpdate = None

        # get the list of the relevant information with the index
        for i, book in enumerate(library): # enumerate means list (or pull out the information?)
            # check if the ISBN entered matches any of the ISBN in the library list
            if book["isbn"] == isbnUpdate:
                # update the index if it matches
                indexUpdate = i
                break

        # continue from previous step
        if indexUpdate is not None:
            # get the book with the given ISBN that user has entered
            book = library[indexUpdate]
            # prompt the relevant information for user to verify (so they know what they want to change)
            print("Book found. Please find the existing information stored in the library below:")
            header = "ISBN\t\t\t\tBook Title\t\t\t\t\t\t\t\t\tType of Book\t\tQuantity Available"
            print(header)
            truncated_isbn = book['isbn'][:15] if len(book['isbn']) < 15 else book['isbn']
            print(f"{truncated_isbn:<18}\t{book['title'][:40]:<40}\t{book['type']:<18}\t{book['quantity']}")

            while True:
                # provide options for users instead of prompting everything
                print("Please select the information you wish to update:")
                print("1. Update title of the book")
                print("2. Update type of the book")
                print("3. Update quantity of the book")
                print("0. Exit")

                # get user's option on which information to update
                updateOption = input("Enter your choice (0-3): ")

                # update information for the title of the book
                if updateOption == "1":
                    title = input("Please enter the new title of the book: ")
                    library[indexUpdate]["title"] = title
                    print("Title of the book has updated successfully!")

                # update information for the type of the book
                elif updateOption == "2":
                    while True:
                        bookType = input("Please enter the type of book with the following types (Hard Cover, Paper Back, eBook): ")
                        if bookType in bookTypes:
                            library[indexUpdate]["type"] = bookType
                            print("Type of the book has updated successfully!")
                            break
                        else:
                            print("Invalid book type. Please choose from Hard Cover, Paper Back, or eBook.")

                # update information for the quantity of the book
                elif updateOption == "3":
                    while True:
                        try:
                            quantity = int(input("Please enter the quantity of the book: "))
                            if quantity < 0:
                                print("Quantity cannot be less than zero. Please enter a non-negative number.")
                            else:
                                library[indexUpdate]["quantity"] = quantity
                                print("Quantity of the book has updated successfully!")
                                break
                        except ValueError:
                            print("Invalid quantity. Please enter a valid number for the quantity of the book.")

                # exit
                elif updateOption =="0":
                    return

                # error message prompted if options is invalid
                else:
                    print("Invalid choice. Please enter a number from 0 to 3.")

        # prompt error message the ISBN is not found in the library list
        else:
            print("Book with the given ISBN not found in the library. Please try again.")

# function 3 - Remove Existing Book
def RemoveExistingBook():
    while True:
        # Get the ISBN of the book that user wishes to remove
        removeISBN = input("Please enter the ISBN of the book you wish to remove (enter '0' to exit): ")

        if removeISBN.lower() == '0':
            return

        removeIndex = None
        for i, book in enumerate(library):
            if book["isbn"] == removeISBN:
                removeIndex = i
                break

        if removeIndex is not None:
            bookToRemove = library[removeIndex]
            while True:
                confirmation = input(f"Remove '{bookToRemove['title']}' with ISBN '{bookToRemove['isbn']}' from the library? (yes/no): ")
                if confirmation.lower() == "yes":
                    removedBook = library.pop(removeIndex)
                    print(f"Book '{removedBook['title']}' with ISBN '{removedBook['isbn']}' has been removed.")
                    break
                elif confirmation.lower() == "no":
                    print("Removal has been cancelled.")
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            break
        else:
            print("Book with the given ISBN not found in the library. Please try again.")

#function 4 - View Books
def ViewBooksInLibrary():
    print("Library Books:")
    header = "ISBN\t\t\t\tBook Title\t\t\t\t\t\t\t\t\tType of Book\t\tQuantity Available"
    print(header)

    # initialize the total quantity of books
    totalQuantity = 0

    for book in library:
        lengthOfIsbn = book['isbn'][:15] if len(book['isbn']) < 15 else book['isbn']
        print(f"{lengthOfIsbn:<18}\t{book['title'][:40]:<40}\t{book['type']:<18}\t{book['quantity']}")

        # the application displays the total number of books in the view book function
        totalQuantity += book['quantity']

    print(f"\nTotal quantity of books in library: {totalQuantity}")

# function 5 - Search Book
def BookSearching():
    while True:
        searchOption = input("Search by:\n1. ISBN\n2. Book Title\n3. Type of Book\n0. Exit\nPlease enter your choice (0-3): ")

        if searchOption == "1":
            # search by ISBN
            searching = input("Please enter the ISBN to search: ")
            # check if the book with the isbn is in the library
            booksMatched = [book['isbn'] for book in library if book['isbn'] == searching]
            if booksMatched:
                searchField = "isbn"
                break
            # error message if cannot find the book with the isbn in library
            else:
                print("No book found with the ISBN in the library.")

        elif searchOption == "2":
            # search by title or keywords
            searching = input("Please enter the title or keywords to search: ")
            # remove spaces
            if searching.strip():
                titlesMatched = [book['title'] for book in library if searching.lower() in book['title'].lower()]
                if titlesMatched:
                    searchField = "title"
                    break
                else:
                    print("No books found with that title in the library.")
            else:
                print("Invalid book title. Please enter a non-empty title.")

        elif searchOption == "3":
            # search by book types
            searching = input("Please enter the type of book to search: ")
            if searching in ["Hard Cover", "Paper Back", "eBook"]:
                searchField = "type"
                break
            else:
                print("Invalid book type. Please choose from Hard Cover, Paper Back, or eBook.")
        elif searchOption == "0":
            return
        else:
            print("Invalid choice. Please enter a number from 0 to 3.")

    booksFound = []
    for book in library:
        if searching.lower() in book[searchField].lower():
            booksFound.append(book)

    if booksFound:
        print("Found Books:")
        header = "ISBN\t\t\t\tBook Title\t\t\t\t\t\t\t\t\tType of Book\t\tQuantity Available"
        print(header)
        for book in booksFound:
            lengthOfIsbn = book['isbn'][:15] if len(book['isbn']) < 15 else book['isbn']
            print(f"{lengthOfIsbn:<18}\t{book['title'][:40]:<40}\t{book['type']:<18}\t{book['quantity']}")
    else:
        print("No books found with that search criteria.")

# function 6 - Borrow Book
def BorrowBook():
    while True:
        searchOption = input("Please search the book that you wish to borrow by the below options:\n1. ISBN\n2. Book Title\n0. Exit\nPlease enter your choice (0-2): ")

        # to exit
        if searchOption =="0":
            break

        # search by ISBN
        if searchOption == "1":
            searching = input("Please enter the ISBN to search: ")
            searchField = "isbn"

        # search by title or keywords
        elif searchOption == "2":
            searching = input("Please enter the title or keywords to search: ")
            searchField = "title"
        else:
            print("Invalid choice. Please enter 0 to 2.")
            # continue to loop
            continue

        booksFound = []
        for book in library:
            if searching.lower() in book[searchField].lower():
                booksFound.append(book)

        if not booksFound:
            print("No books found with that search criteria.")
            continue

        print("Found Books:")
        header = "ISBN\t\t\t\tBook Title\t\t\t\t\t\t\t\t\tType of Book\t\tQuantity Available"
        print(header)
        for book in booksFound:
            lengthOfIsbn = book['isbn'][:15] if len(book['isbn']) < 15 else book['isbn']
            print(f"{lengthOfIsbn:<18}\t{book['title'][:40]:<40}\t{book['type']:<18}\t{book['quantity']}")

        while True:
            isbnBorrow = input("Please enter the ISBN of the book you wish to borrow (enter '0' to cancel): ")
            if isbnBorrow == '0':
                break  # Exit the inner loop and return to the main menu

            indexBorrow = None

            # get the index of the book with the ISBN that user has entered
            for i, book in enumerate(library):
                if book["isbn"] == isbnBorrow:
                    indexBorrow = i
                    break

            if indexBorrow is not None:
                bookBorrowed = library[indexBorrow]
                while True:
                    try:
                        quantityBorrowed = int(input(f"Please enter the number copies of '{bookBorrowed['title']}' you wish to borrow: "))
                        if quantityBorrowed > 0 and quantityBorrowed <= bookBorrowed['quantity']:
                            bookBorrowed['quantity'] -= quantityBorrowed
                            isbn = bookBorrowed['isbn']
                            if isbn in borrowedCount:
                                borrowedCount[isbn] += quantityBorrowed
                            else:
                                borrowedCount[isbn] = quantityBorrowed

                            borrowedBooks.append({"isbn": bookBorrowed['isbn']})

                            print(f"{quantityBorrowed} copies of '{bookBorrowed['title']}' have been borrowed.")
                            print(f"Updated quantity available in the library: {bookBorrowed['quantity']}")
                            print("***** Please return the book(s) within 30 days to avoid any fine *****")
                            break
                        else:
                            print("Invalid quantity. Please enter a valid number of copies to borrow.")
                    except ValueError:
                        print("Invalid input. Please enter a valid positive integer.")
            else:
                print("Book with the given ISBN not found in the library.")

# function 7 - Return Book
def ReturnBook():
    while True:
        isbnReturn = input("Please enter the ISBN of the book you wish to return (enter '0' to cancel): ")

        if isbnReturn == '0':
            break

        indexReturn = None

        for i, book in enumerate(library):
            if book["isbn"] == isbnReturn:
                indexReturn = i
                break

        if indexReturn is not None:
            bookReturned = library[indexReturn]
            while True:
                try:
                    quantityReturned = int(input(f"Please enter the number of copies of '{bookReturned['title']}' you wish to return: "))
                    if quantityReturned > 0:
                        bookReturned['quantity'] += quantityReturned
                        print(f"{quantityReturned} copies of '{bookReturned['title']}' have been returned.")
                        print(f"Updated quantity available in the library: {bookReturned['quantity']}")
                        return
                    else:
                        print("Invalid quantity. Please enter a valid number of copies to return.")
                except ValueError:
                    print("Invalid input. Please enter a valid number of copies to return.")
        else:
            print("Book with the given ISBN not found in the library.")

# function 8 - Summary on Borrowed Book
def SummaryBorrowedBook():
    # if any books have been borrowed
    borrowedBooksExist = False

    for borrowedBook in borrowedBooks:
        isbn = borrowedBook['isbn']
        quantityBorrowed = borrowedCount.get(isbn, 0)

        # get the book information using the ISBN
        bookInfo = next((book for book in library if book['isbn'] == isbn), None)

        if bookInfo:
            if not borrowedBooksExist:
                print("Borrowed Books Information:")
                header = "ISBN\t\t\t\tBook Title\t\t\t\t\t\t\t\t\tType of Book\t\tQuantity Borrowed"
                print(header)
                borrowedBooksExist = True

            length_of_isbn = isbn[:15] if len(isbn) < 15 else isbn
            print(f"{length_of_isbn:<18}\t{bookInfo['title'][:40]:<40}\t{bookInfo['type']:<18}\t{quantityBorrowed}")

    if not borrowedBooksExist:
        print("No books have been borrowed.")

# calculate overdue days function
def calculateOverdueDays(dueDate):
    # to get today's date
    today = datetime.date.today()
    # calculation on overdue days
    overdueDays = (today - dueDate).days
    return max(overdueDays, 0)

# calculate fine function - using overdue days
def calculateFine(dueDate):
    overdueDays = calculateOverdueDays(dueDate)
    # calculate fine if overdue by any amount (start from the date of borrow)
    if overdueDays > 0:
        amountOfFine = overdueDays * finePerDay
        return amountOfFine, overdueDays
    else:
        return 0, overdueDays

# function 9 - Fine Management
def fineManagement():
    while True:
        searchOption = input("Search by:\n1. ISBN\n0. Exit\nEnter your choice (0-1): ")

        if searchOption == "0":
            return

        elif searchOption == "1":
            isbn = input("Please enter the ISBN: ")
            borrowedBook = next((book for book in borrowedBooks if book['isbn'] == isbn), None)
            if borrowedBook:
                bookInfo = next((book for book in library if book['isbn'] == isbn), None)
                if bookInfo:
                    quantityBorrowed = borrowedCount.get(isbn, 0)
                    print("Borrowed Books Information:")
                    header = "ISBN\t\t\t\tBook Title\t\t\t\t\t\t\t\t\tType of Book\t\tQuantity Borrowed"
                    print(header)
                    borrowedBooksExist = True

                    lengthOfIsbn = isbn[:15] if len(isbn) < 15 else isbn
                    print(f"{lengthOfIsbn:<18}\t{bookInfo['title'][:40]:<40}\t{bookInfo['type']:<18}\t{quantityBorrowed}")

                    borrowDateInput = input("Please enter the borrowing date (ddMMyyyy): ")

                    try:
                        day = int(borrowDateInput[:2])
                        month = int(borrowDateInput[2:4])
                        year = int(borrowDateInput[4:])
                        borrowDate = datetime.date(year, month, day)

                        if borrowDate > datetime.date.today():
                            print("Invalid date. Please enter a date in the past.")
                            continue

                        dueDate = borrowDate + datetime.timedelta(days=30)
                        amountOfFine, overdueDays = calculateFine(dueDate)

                        if amountOfFine > 0:
                            print(f"Overdue days: {overdueDays}")
                            print(f"Fine Amount for '{bookInfo['title']} (ISBN {isbn})': ${amountOfFine:.2f}")
                        else:
                            print(f"No fine for '{bookInfo['title']}' (ISBN {isbn}).")
                    except ValueError:
                        print("Invalid date format. Please enter a valid date.")
                else:
                    print(f"Book with ISBN {isbn} not found in the library.")
            else:
                print(f"No borrowed books found with ISBN {isbn}.")

        else:
            print("Invalid choice. Please enter 1 or 2.")


# validation for ISBN
def isbnValidation(isbn):
    # remoce hyphens
    isbn = isbn.replace('-', '').replace(' ', '')

    isbnDigits = []

    for digit in isbn:
        if digit.isdigit():
            isbnDigits.append(int(digit))
        elif digit.upper() == 'X':
            isbnDigits.append(10)
        else:
            return False

    # ISBN 10
    if len(isbnDigits) == 10:
        checkDigit = 0
        for i in range(9):
            checkDigit += (i + 1) * isbnDigits[i]
        checkDigit %= 11
        return checkDigit == isbnDigits[9]

    # ISBN 13
    if len(isbnDigits) == 13:
        sum = 0
        for i in range(12):
            if i % 2 == 0:
                sum += isbnDigits[i]
            else:
                sum += 3 * isbnDigits[i]
        checkDigit = (10 - sum % 10) % 10
        return checkDigit == isbnDigits[12]

    # ISBN cannot be less than 10 digits
    if len(isbn) != 10:
        return False

    # compute the first 9 digits
    _sum = 0
    for i in range(9):
        if 0 <= int(isbn[i]) <= 9:
            _sum += int(isbn[i]) * (10 - i)
        else:
            return False

    # check the last digit
    if(isbn[9] != 'X' and
            0 <= int(isbn[9]) <= 9):
        return False

    # add the value, X = 10
    _sum += 10 if isbn[9] == 'X' else int(isbn[9])

    # check if the sum can be devided by 11
    return (_sum % 11 == 0)

    return False