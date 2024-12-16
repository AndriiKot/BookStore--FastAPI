import json

path_books = "./data/books.json"

def load_books():
    with open(path_books, 'r') as file:
        return json.load(file)

def save_books(books):
    with open(path_books, 'w') as file:
        json.dump(books, file)

def find_book_by_id(book_id):
    books = load_books()
    for book in books:
        if book["id"] == book_id:
            return book
    return None

