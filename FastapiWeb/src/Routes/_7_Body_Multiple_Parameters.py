from email.policy import default
from typing import Union
from fastapi import FastAPI, Path, Query, Body

from Models._7_Body_Multiple_Parameters import Item, User

app = FastAPI()

# Mixing path, query and body parameters
@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int=Path(default=..., title="Id of the item"), # path parameter
    q: str=Query(default=None, alias="item-query"), # query parameter
    item: Union[Item, None] = None, # body parameter
):
    result = {"item_id":item_id}
    if q:
        result.update({"q":q})
    if item:
        result.update({"Item":item})
    return result

# Multiple body parameters
@app.put("/items1/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    result = {"item_id": item_id, "item": item, "user": user}
    return result

# Declaring single parameter as a body parameter
@app.put("/items2/{item_id}")
async def update_item(
    item_id: int, 
    item: Item, 
    user: User, 
    importance: int=Body(default=None)
):
    result = {"item_id": item_id, "item": item, "user": user, "importance": importance}
    return result

# Embeding key into body parameter
@app.put("/items3/{item_id}")
async def update_item(item_id: int, item: Item=Body(default=None, embed=True)):
    result = {"item_id": item_id, "item": item}
    return result