from fastapi import FastAPI, HTTPException
import uvicorn
import os
import argparse
import json

path_version = "../version.json"
path_books = "./data/books.json"

def load_books():
    with open(path_books, 'r') as file:
        return json.load(file)

def load_version():
    with open(path_version) as f:
        return json.load(f)["version"]

app = FastAPI(
    title="Bookstore",
    description="Simple REST API for a bookstore",
    version=load_version()
)


@app.get(
    path="/books",
    tags=["Books 📚" ],
    summary="Get all books",
)
async def get_books():
    books = load_books()
    return books

@app.get(
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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the FastAPI app.")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the app on.")
    args = parser.parse_args()

    module_name = os.path.splitext(os.path.basename(__file__))[0]
    uvicorn.run(module_name + ":app", host="127.0.0.1", port=args.port, reload=True)
