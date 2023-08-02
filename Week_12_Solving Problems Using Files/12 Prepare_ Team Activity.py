#-12 Prepare: Team Activity
#-Finding Items in a File

with open("books.txt") as books_scriptures:

  option_scripture = input("Hello, Which scripture would you like to know about?")
  largest_chapters = 0
  largest_book = ""

  for scriptures in books_scriptures:
    
    scriptures = scriptures.strip()
    scriptures = scriptures.split(":")

    book = scriptures[0]
    chapters = int(scriptures[1])
    scripture = scriptures[2]

    if scripture.lower() == option_scripture.lower():
      print(f"Scripture: {scripture}, Book: {book}, Chapters: {chapters}")

      if (scripture.lower() == option_scripture.lower()) and (chapters > largest_chapters):
        largest_chapters = chapters
        largest_book = book

print(f"\nThe largest number of chapters are {largest_chapters} in the book of {largest_book}")


    
    
  














    
    


