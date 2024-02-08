'''
Author : Cheng Sheh Nee
Admin No / Grp : 234745J / AA2301
'''

from Functions import LogIn, AddNewBook, UpdateExistingBook, RemoveExistingBook, ViewBooksInLibrary, BookSearching, BorrowBook, ReturnBook, SummaryBorrowedBook, fineManagement

# main menu loop
while True :
    if LogIn():
        while True:
            print("--- MINI LIBRARY MANAGEMENT SYSTEM ---")
            print("1. Add New Book")
            print("2. Update Existing Book")
            print("3. Remove Existing Book")
            print("4. View Books")
            print("5. Search Book")
            print("6. Borrow Book")
            print("7. Return Book")
            print("8. Summary - Borrowed Books")
            print("9. Fine Management")
            print("0. Quit")
            choice = input("Please enter your choice (0-9): ")


            if choice == '1':
                AddNewBook()
            elif choice == '2':
                UpdateExistingBook()
            elif choice == '3':
                RemoveExistingBook()
            elif choice == '4':
                ViewBooksInLibrary()
            elif choice == '5':
                BookSearching()
            elif choice == '6':
                BorrowBook()
            elif choice == '7':
                ReturnBook()
            elif choice == '8':
                SummaryBorrowedBook()
            elif choice == '9':
                fineManagement()
            elif choice == '0':
                print("Thank you for using the Library Management System. Goodbye!")
                exit()
            else:
                print("Invalid choice. Please try again.")