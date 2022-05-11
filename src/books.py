from fastapi import FastAPI
from enum import Enum

app = FastAPI()

BOOKS = {
    'book1':{'title':'Title1','Author':'Author1'},
    'book2':{'title':'Title2','Author':'Author2'},
    'book3':{'title':'Title3','Author':'Author3'},
    'book4':{'title':'Title4','Author':'Author4'},
    'book5':{'title':'Title5','Author':'Author5'},
}

@app.get("/")
async def get_all_books():
    return BOOKS


@app.get("/books/mybook")
async def read_favourite_book():
    return {"title":"My favourite book"}

# path parameter API has to be under any API that follow the same path
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