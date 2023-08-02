with open("books.txt") as files_books:
    for book in files_books:
        book = book.strip()
        print(book)