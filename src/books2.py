from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

# Uses BaseModel to enforce type hinting
class Book(BaseModel):
    id:UUID
    title:str = Field(min_length=1) # data validation 
    author:str = Field(min_length=1, max_length=100)
    description:Optional[str] = Field(
        title="Description of book",
        max_length=100,
        min_length=1)
    rating:int = Field(gt=-1,lt=101)

    class Config:
        schema_extra = {
            "example":{
                "id":"94b47336-8ff8-4efe-bf89-981832ae6555",
                'title':"Title_1",
                "author":"Author_1",
                "description":"A very Nice Book",
                "rating":75
            }
        }

BOOKS = []

@app.get("/")
async def read_all_books(books_to_return:Optional[int]=None):
    if len(BOOKS) < 1:
        create_books_no_api()
    if books_to_return and len(BOOKS) >= books_to_return>0:
        i = 1
        new_books = []
        while i <= books_to_return:
            new_books.append(BOOKS[i-1])
            i +=1
        return new_books
    return BOOKS

@app.get("/book/{book_id}")
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id ==book_id:
            return x

@app.post("/")
async def create_book(book:Book):
    BOOKS.append(book)
    return book

@app.put("/{book_id}")
async def update_book(book_id:UUID, book:Book):
    counter = 0
    for x in BOOKS:
        counter +=1
        if x.id == book_id:
            BOOKS[counter-1] = book
            return BOOKS[counter-1]

@app.delete("/{book_id}")
async def delete_book(book_id:UUID):
    counter = 0
    for x in BOOKS:
        counter +=1
        if x.id == book_id:
            del BOOKS[counter-1]
            return f'ID:{book_id} deleted'

def create_books_no_api():
    book_1 = Book(
        id="97a28667-592b-453e-a962-2b34c44e95f5",
        title = "Title_1",
        author = "Author_1",
        description = "Description_1",
        rating = 50
    )
    book_2 = Book(
        id="8a36dd3c-fe03-43c5-97a7-6185dd95c084",
        title = "Title_2",
        author = "Author_2",
        description = "Description_2",
        rating = 60
    )
    book_3 = Book(
        id="94b47336-8ff8-4efe-bf89-981832ae6555",
        title = "Title_3",
        author = "Author_3",
        description = "Description_3",
        rating = 70
    )
    BOOKS.append(book_1)
    BOOKS.append(book_2)
    BOOKS.append(book_3)