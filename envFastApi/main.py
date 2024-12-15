import uvicorn
import os
import argparse
from fastapi import FastAPI
from routers.books import router as books_router
from utils.load_version import load_version

app = FastAPI(
    title="Bookstore",
    description="Simple REST API for a bookstore",
    version=load_version(),
)

app.include_router(books_router)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the FastAPI app.")
    parser.add_argument("--port", type=int, default=8000, help="Port to run the app on.")
    args = parser.parse_args()

    module_name = os.path.splitext(os.path.basename(__file__))[0]
    uvicorn.run(module_name + ":app", host="127.0.0.1", port=args.port, reload=True)
