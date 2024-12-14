from fastapi import FastAPI
import uvicorn
import os

app = FastAPI()

books = [
	{
        "id": 1,
        "title": "Python Programming",
		"author": "John Doe",
		"price": 19.99
	},
    {
		"id": 2,
        "title": "FastAPI",
		"author": "John Doe",
		"price": 29.99
	}
]

@app.get("/books")
async def get_books():
	return books

if __name__ == "__main__":
    module_name = os.path.splitext(os.path.basename(__file__))[0]
    uvicorn.run(module_name + ":app", host="127.0.0.1", port=8000, reload=True)
