# Create a dictionary of book titles and their authors. Write a function to search for a book
# by its title and return the author's name.
def get_after(books,name_book):
    after = "dont have this book"
    for k, v in books.items():
        if v == name_book:
            after = k
    return after
books = {"H.Tumanyan":"Sasuntsi Davit","Rafi":"Samvel"}
print(get_after(books, "Samvel"))


