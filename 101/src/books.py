from typing import Optional
from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    'book_1':{'title':'Title_1','author':'Author_1'},
    'book_2':{'title':'Title_2','author':'Author_2'},
    'book_3':{'title':'Title_3','author':'Author_3'},
    'book_4':{'title':'Title_4','author':'Author_4'},
    'book_5':{'title':'Title_5','author':'Author_5'},
}

@app.get("/")
async def get_all_books():
    return BOOKS

@app.get("/books/skipbook")
async def skip_books(skip_book: Optional[str] = None):
    if skip_books:
        new_books = BOOKS.copy()
        del new_books[skip_book]
        return new_books
    return BOOKS

@app.get("/books/mybook")
async def read_favourite_book():
    return {"title":"My favourite book"}

# parameter API has to be under any path parameter API that follow the same path
# /books/mybook will not work if below /books/{param}
@app.get("/books/{book_title}")
async def read_book(book_title):
    return {"title":book_title}

@app.get("/books/{book_id}")
async def read_book_id(book_id:int):
    return {"book_id":book_id}

@app.get("/{book_name}")
async def read_book(book_name:str):
    return BOOKS[book_name]

# Using Enum to create drop downlist for parameters
class DirectionName(str, Enum):
    north = "North"
    south = "South"
    east = "East"
    west = "West"

@app.get("/directions/{direction_name}")
async def get_direction(direction_name: DirectionName):
    if direction_name == DirectionName.north:
        return{"Direction":direction_name, "sub":"Up"}
    if direction_name == DirectionName.west:
        return{"Direction":direction_name, "sub":"Left"}
    if direction_name == DirectionName.east:
        return{"Direction":direction_name, "sub":"Right"}
    return{"Direction":direction_name, "sub":"Down"}

@app.post("/")
async def create_book(title, author):
    current_book_id = 0
    if len(BOOKS) > 0:
        for book in BOOKS:
            x = int(book.split("_")[-1])
            if x > current_book_id:
                current_book_id = x
    BOOKS[f'book_{current_book_id+1}'] = {'title':title,'author':author}
    return BOOKS[f'book_{current_book_id+1}']

@app.put("/{book_name}")
async def update_book(book_name:str, title:str, author:str):
    book_information = {'title':title, 'author':author}
    BOOKS[book_name] = book_information
    return book_information

@app.delete("/{book_name}")
async def delete_book(book_name):
    del BOOKS[book_name]
    return f'{book_name} deleted'

# query parameter end with a forward slash
@app.get("/assignment/")
async def read_book_assignment(book_name:str):
    return BOOKS[book_name]
