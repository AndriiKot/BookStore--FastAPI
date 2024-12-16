from fastapi import APIRouter, HTTPException
from models.book import NewBook
from services.book_service import load_books, save_books, find_book_by_id

router = APIRouter()

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
    book = find_book_by_id(book_id)
    if book:
        return book
    raise HTTPException(status_code=404, detail="Book not found")

@router.post(
    path="/books",
    tags=["Books 📚"],
)
async def create_book(new_book: NewBook):
    books = load_books()
    new_id = len(books) + 1
    books.append({
        "id": new_id,
        "title": new_book.title,
        "author": new_book.author
    })
    save_books(books)
    return {"success": True, "message": "Book created successfully"}
