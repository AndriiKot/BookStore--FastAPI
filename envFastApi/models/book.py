from pydantic import BaseModel

class NewBook(BaseModel):
    title: str
    author: str


