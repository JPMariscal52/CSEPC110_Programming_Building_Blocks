#-10 Prepare: Preparation Material


books = ['lofr', 'hobbit', 'silver', 'gold', 'red']

number_of_books = len(books)
print(number_of_books)

for i in range(1,len(books)):
    book = books[i]
    print(book)
    print(i)

for book in books:
  print(book)

for i in range(len(books)):
    book = books[i]
    print(f"{i}. {book}")


names = ['Benjamin', 'Tania', 'Jafet', 'Helaman', 'Patricio']
numbers = [2221547655, 2223596889, 2228640554, 2225784859, 8999658536]

for i in range(len(names)):
    name = names[i]
    number = numbers[i]

    print(f"{name} - {number}")