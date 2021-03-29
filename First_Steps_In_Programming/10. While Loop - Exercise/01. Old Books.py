favourite_book = input()
next_book = input()
checked_books = 0
book_is_found = False
while next_book != "No More Books":
    if next_book == favourite_book:
        book_is_found = True
        break
    checked_books += 1
    next_book = input()
if book_is_found:
    print(f'You checked {checked_books} books and found it.')
else:
    print("The book you search is not here!")
    print(f'You checked {checked_books} books.')
