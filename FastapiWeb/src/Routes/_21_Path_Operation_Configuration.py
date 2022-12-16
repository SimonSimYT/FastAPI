from doctest import debug_script
from urllib import response
from fastapi import FastAPI, status
from Models._21_Path_Operation_Configuration import Item
from Resources._21_Path_Operation_Configuration import Tags
app = FastAPI()

@app.post(
    "/items/", 
    response_model=Item, 
    status_code=status.HTTP_201_CREATED, 
    tags=["items"])
async def create_item(item: Item):
    return item

@app.get("/items/", tags=["items"])
async def read_items():
    return [{"name":"Foo", "price":42}]

@app.get("/users/", tags=["users"])
async def read_users():
    return [{"username":"johndoe"}]

# Using Enum for tags
@app.get("/items1/", tags=[Tags.items])
async def read_items():
    return [{"name":"item", "price":42}]

@app.get("/users1/", tags=[Tags.users])
async def read_user():
    return ["Rick", "Morty"]

# Adding Summary and description
@app.post(
    "/items3", 
    response_model=Item, 
    summary="Summary - Create an item", 
    description="Description - This is a description",
)
async def create_item(item: Item):
    return item

# Description from docstring, fastapi will read it from there
