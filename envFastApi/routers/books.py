from fastapi import APIRouter, HTTPException
from models.book import NewBook
import json

router = APIRouter()
path_books = "./data/books.json"


def load_books():
    with open(path_books, 'r') as file:
        return json.load(file)

@router.get(
    path="/books",
    tags=["Books 📚"],
    summary="Get all books",
)
async def get_books():
    books = load_books()
    return books

@router.get(
    path="/books/{book_id}",
    tags=["Books 📚"],
    summary="Get a book by ID",
)
async def get_book(book_id: int):
    books = load_books()
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")


@router.post(
    path="/books",
    tags=["Books 📚"],)
async def create_book(new_book: NewBook):
    books = load_books()
    books.append({
        "id": len(books) + 1,
        "title": new_book.title,
        "author": new_book.author
    })
    return {"success": True, "message": "Book created successfully"}
